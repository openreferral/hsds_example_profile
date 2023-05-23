# HSDS Example Profile

Replace this file with information about your profile.

## Setup environment for docs and schema tools

Set up an environment and install Python dependencies into it:

```
python3 -m venv .ve    
source .ve/bin/activate
pip install -r requirements.txt
```


## Building schemas, datapackage.json, examples and compiled schemas

You need to define a place where your profile is going to exist on the web.  Most commonly this can be on github, for this repository it would be `https://github.com/openreferral/hsds_example_profile`. So you would run the folling in the root of this repo:

```
hsds_schema.py profile-all https://github.com/openreferral/hsds_example_profile --clean
```
This will generate:

* Schema files from the profile
* datapackage.json
* openapi.json
* compiled schemas
* examples

At some point this will also generate:

 * ERD diagram
 * Database scripts


## How it Works

In order to make a profile you need to modify files in the `profile` directory and modify this README.md. Nothing else should be needed.  Everything else can be generated running the previous command.

The `profile` directory should contain a file for every JSON file in the [core schema directory](https://github.com/openreferral/specification/tree/3.0/schema) that needs changing.  You should not copy the whole file from the core schemas, just make the JSON you supply match the structure of the parts you want to change.  It uses the [JSON Merge Patch](https://datatracker.ietf.org/doc/html/rfc7386) algorithm to patch the core schemas with the ones in your profile.
Also, if you want to remove any keys then you put `null` against the value. If you want to remove a whole file then just supply the file with just `null` in it.

## This Example Profile

The most common JSON you want to override is `profile/openapi.json`.  This contains the Open API definition of the profile. 

`profile/openapi.json`

```
{
  "info": {
    "title": "HSDS OpenAPI Demo Profile",
    "version": "3.0",
    "description": "Demo Profile" ,
    "contact": null,
    "summary": null,
    "license": {
      "name": "Creative Commons Attribution Share-Alike 4.0 license",
      "url": "https://creativecommons.org/licenses/by/4.0/"
    }
  }
}
```
This will patch the core open API file with new info, removing the `contact` and `summary` fields and will keep the rest of the file the same.

There also contains a `profile/service.json`:

```
{
   "properties": {
     "fees": null,
     "fees_description": null
   },
   "allOf": [
     {"required": ["url"]} 
   ]
}
```

This removes `fees` and `fees_description` in the profile.  It also adds `url` to the required fields.  
Adding an `allOf` block is preferred over replacing the original `required` list.  Many additional conditions specific to the profile can be added to this `allOf` array.

In this example profile `metadata` objects are not required. So the file `metadata.json` just has a `null` in it.  The tool will remove all references to `metadata.json` too.

Also you can add a `profile/data` directory that JSON files that contain any default data required in the profile.  This can be used for defining taxonomies that are required in the profile.  The JSON files in this folder should be named the same as the schema files and contain and array of the correspoinding data.
