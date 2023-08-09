# HSDS Example Profile

This is the HSDS Example Profile repository. It contains many of the tools required to develop and establish a new HSDS Profile.

You should use this repository as a template or a minimal base from which to begin developing your own HSDS Profile; this is much easier than doing it by yourself from scratch!

This README contains documentation on how the HSDS Profiles mechanism works at a technical level and some examples of common things you may want to do with a Profile. You will likely want to remove the example changes before implementing your own.

When you are finished, you should replace the contents of this README with contents relevant to your HSDS Profile such as an overview, how to contribute, and where to find documentation.

## Getting Started

To create a Profile based on this template you should do the following:

1. Clone, Fork, or download this repository [as a zip file](https://github.com/openreferral/hsds_example_profile/archive/main.zip)
2. Ensure that the git remote URLs are pointed towards your new repository
3. Set up the environment by installing requirements
4. Develop your Profile by defining changes to HSDS schema files
5. Use the HSDS Schema tools to automatically generate your Profile schema file
6. Generate some documentation for your Profile, and edit it to provide more content if useful
7. Push your Profile repository to a public location (usually Github or Gitlab)
8. Wire your documentation into [Readthedocs](https://readthedocs.org/)

Technically speaking the use of git, Github, or Gitlab is optional. However, these tools / platforms do provide good integration into documentation services such as Readthedocs and enable you to govern your Profile collaboratively with others by supporting Issue tracking and some project management. Therefore, we recommend them.

## Set up the environment for generating schemas and docs

This repository relies on some Python tools to support generating your final Profile schema files. It is also planned that this repository can support you automatically generating some basic documentation for your Profile, which will also rely on some python tools.

This works by creating a [Python Virtual Environment](https://docs.python.org/3/library/venv.html) within the repository folder on your computer, and then the dependencies are installed into it. This means that they won't interfere with any other Python projects or libraries on your computer, and we can tightly control the versions of libraries used for this template so that it won't break.

If you do not have Python installed on your platform, you should do so now before proceeding with the setup. You will also need [Pip](https://pypi.org/project/pip/), to install Python packages.

### Initial setup

Inside the repository folder, run the following commands in sequence to set up a virtual environment and install Python dependencies into it:

```
python3 -m venv .ve    
source .ve/bin/activate
pip install -r requirements.txt
```

If there are any errors, please report them using the [Issue Tracker](https://github.com/openreferral/hsds_example_profile/issues) for this project. Please include details of your system and Python environments.

This installs several tools used in this repository, including the [HSDS Schema Tools](https://github.com/openreferral/hsds_schema_tools). If you experience errors using the HSDS Schema Tools, please report them using the [HSDS Schema Tools Issue Tracker](https://github.com/openreferral/hsds_schema_tools/issues) rather than the issue tracker for this repository.

Now you're all set up! From now on, whenever you need to generate your Profile schemas or documentation you will need to activate the Python virtual environment within your Profile repository folder:

```
source .ve/bin/activate
```

To deactivate, run:

```
deactivate
```

### Updating

It is unlikely that you will need to update the libraries in the environment, but it may be that we improve or update the HSDS Schema tools etc. To do this you can run:

```
pip install --upgrade -r requirements.txt
```

## Developing your Profile

This section contains detailed guidance on how to develop your Profile by defining changes to the core HSDS Schemas.

### Overview and Basic Workflow

HSDS Profiles work by either *extending* or *overriding* existing HSDS Schema files:

* Extending &ndash; defining new property, codelists, taxonomies, API endpoints, and constraints on existing properties
* Overriding &ndash; removing properties and constraints which are defined by the [HSDS Schema Reference](http://docs.openreferral.org/en/latest/hsds/schema_reference.html) or the [HSDS API Reference](http://docs.openreferral.org/en/latest/hsds/api_reference.html)

HSDS is implemented in [JSON Schema](http://json-schema.org/) so you should be somewhat familiar with this to implement any changes to the HSDS schemas. The API specification is implemented in [OpenAPI JSON](https://spec.openapis.org/oas/latest.html#openapi-specification), so familiarity with this is recommended for changes to the HSDS API Specification.

The basic workflow of implementing a HSDS Profile is as follows:

* Define your changes to specific [HSDS schema files](https://github.com/openreferral/specification/tree/3.0/schema) or the `openapi.json` file.
* Use [HSDS Schema Tools](https://github.com/openreferral/hsds_schema_tools/tree/main) to generate compiled schemas and examples for your Profile, making it ready to use.

After you're done, you should prepare some documentation for your Profile and of course share it with the community.

### The structure of this repository

To develop your HSDS Profile you will need to be working in a specific folder, so it is worthwhile taking a quick look at the structure of this repository:

```
├─ examples/ (A directory containing automatically generated examples. You should NOT edit this folder manually.)
├─ profile/ (The directory containing all of the changes representing your Profile. You MUST be editing files here manually.)
├─ schema/ (A directory containing automatically generated schemas created by combining your changes in the profile directory with the HSDS Schema files. You should NOT edit this folder manually.)
├─ LICENSE (The license file for this repository. The contents of the template repository are licensed by the Creative Commons Attribution Share-Alike 4.0 license. You may license your additional documentation under a different license.)
├─ README.md (This readme file! You SHOULD edit it manually once you're done with your profile, and change it to suit your needs.)
├─ datapackage.json (An automatically generated datapackage file which will allow people to publish data using your profile in a tabular format. You should NOT edit or remove this file.)
```

As you can see, most of your work will be inside the `profile` directory. Most of the rest is generated and handled by the HSDS Schema tools, which you installed during the setup.

### A note on the underlying technologies

HSDS 3.0 is implemented using [JSON Schema](https://json-schema.org/), while the API Specification is described using [OpenAPI](https://spec.openapis.org/) in JSON format. You will need to develop some familiarity with these technologies if you want to implement a Profile.

While the tutorials and examples in this repository aim to be clear and explain the changes that are being made to support new Profile developers who may be encountering these technologies for the first time, they are not intended as a full replacement for the relevant learning materials for either JSON Schema or OpenAPI.

Specific versions:

* HSDS 3.0 is implemented in [JSON Schema Draft 2020-12](http://json-schema.org/specification-links.html#2020-12). This was the latest version available during implementation. You do not need to declare a JSON Schema version in your Profile schema files, but you should take care not to use features that are only available in later versions of JSON Schema and be careful when using features that have a different behaviour in previous versions.
* The HSDS OpenAPI specification file is implemented in [OpenAPI version 3.1.0](https://spec.openapis.org/oas/latest.html), which was the latest version available during implementation. You should therefore ensure that any features you add to your Profile's `openapi.json` file are available in this version.

### Defining changes

Defining changes to the HSDS Schema is what makes your Profile. This is therefore likely going to be the most involved step in creating your Profile.

The Profiles mechanism works by matching files inside the `profile` directory &mdash; which represent your changes &mdash; to corresponding schema files [in the HSDS specification](https://github.com/openreferral/specification/tree/3.0/schema). The HSDS Schema Tools will then perform a [JSON Merge Patch](https://datatracker.ietf.org/doc/html/rfc7386) to produce your Profile schema files inside the `schema` directory. It will then also compile those schema files into the `schema/compiled` directory.

The task, therefore, is to implement your desired changes in [JSON Schema](http://json-schema.org/) inside a file corresponding to a HSDS schema file. The concept is very similar to overriding or extending a template or a view in web development. You should create a new file for each file in the HSDS Schema that you want to change or override.

You should only create files in `profile` which correspond to the parts of the HSDS schema that you want to change. You do *not* need to include files which you want to keep the same in your profile. For example, if your profile only changes the `Service` object, then you only need to create `service.json` and not `organization.json` etc.

Similarly, you should NOT copy the entire schema file from HSDS and make changes. *Only write in the changes you need*. For example, if you were adding a new property `myNewProperty` to `Service`, you would do the following inside `profile/service.json`:

```json
{
  "properties": {
    "myNewProperty": {
      "type": "string",
      "title": "My New Property",
      "Description": "A Description of My New Property, added by my awesome HSDS Profile."
    }
  }
}
```

The reason for this is to ensure that your Profile is only changing the parts of the schema file that you need to change and thereby avoid any accidents. It also keeps things nice and readable for you (and others!) to maintain your Profile. The JSON Merge Patch algorithm will take care of ensuring that your changes are made to the appropriate parts of the schema file.

You can also remove parts of the HSDS schema through the `null` keyword. For example, if you wanted to remove `fees` and `fees_description` from `Service` you would include the following in your `profile/service.json`:

```json
{
  "properties": {
    "fees": null,
    "fees_description": null
  }
}
```

You can also remove entire Objects ("Tables") from the schema by creating a corresponding file in your profile which *only* contains `null`. For example if you wanted to remove `Metadata` objects, you would create `profile/metadata.json` and it would include only the following line:

```json
null
```

Using the same techniques, you can also define changes to the HSDS OpenAPI Specification. Create the `openapi.json` file and make changes. This file is NOT in JSON Schema format, but is a JSON file specifying the HSDS API specification in accordance with [OpenAPI](https://spec.openapis.org/oas/latest.html#versions). You should familiarise yourself with this if you want to make changes to this file.

Finally, you can also define some default data inside of a `profile/data` directory. For each type of default data you want, create a file inside of this directory with a name corresponding to the schema file. The file should then include a JSON-formatted array where each of the items is conformant to the schema associated with it. For example, if you wanted to define some Taxonomy Terms for use with your profile, you should create the file `profile/data/taxonomy_term.json`. This file would then contain a JSON array of [taxonomy_term](http://docs.openreferral.org/en/latest/hsds/schema_reference.html#taxonomy-term) items, where each one represents a term in your taxonomy.

#### Things you probably want to remove from this Example Profile

This Example Profile defines some changes to files to get you started and illustrates how to create some common changes.

You should be aware of these changes so that you don't make an unintentional change to the schema in your Profile. You likely want to remove or edit them explicitly:

* `profile/metadata.json` is set to `null`, removing the HSDS [Metadata schema](http://docs.openreferral.org/en/latest/hsds/schema_reference.html#metadata)
* `profile/openapi.json` overrides the `info` block in the [HSDS API Specification](http://docs.openreferral.org/en/latest/hsds/api_reference.html). You should replace this with the appropriate details of your Profile.
* `profile/service.json` removes the `fees` and `fees_description` properties from the HSDS [Service schema](http://docs.openreferral.org/en/latest/hsds/schema_reference.html#service), and also makes `url` required.
* `profile/data/taxonomy_term.json` defines an example [Taxonomy Term](http://docs.openreferral.org/en/latest/hsds/schema_reference.html#taxonomy-term).

#### Some notes on style and naming conventions

You are permitted to implement your Profile using whatever style and naming conventions you desire, however, you should consider existing HSDS 3.0 conventions to ensure that your Profile is not jarring to use or causes confusion for users.

* Properties names should be in English `en`.
* Property names should be in `lower_case_with_underscores`.
* Don't abbreviate words in properties e.g. use `maximum_attendance` rather than `max_attendance`.
* Where possible, use plurals in property names when describing arrays or lists e.g. `"requirements": []` not `requirement: []`. There are exceptions to this based on English conventions e.g. `funding` rather than `fundings`.
* Property names should not contain the name of their parent e.g. `name` and not `service_name`. This also goes for new objects that you define.

### Building the schema files, datapackage.json, examples, and compiled schemas

Once you've finished defining your changes to your schema files and/or adding default data, you should compile your schema.

Compiling your schema requires that you provide a URI where your profile will live on the web. This must be publicly accessible, as this is what publishers will use to state they are using your profile and what tooling should use to find the profile schemas for validation. As noted earlier, it is sensible to make this a public git repository such as on Github or Gitlab.

Once you have your URI, you should run the HSDS Schema tools command below (make sure you're at the root of your repository!) and supply your URI. For example, the URI for this Example Profile is `https://github.com/openreferral/hsds_example_profile`. The command would be:

```
hsds_schema.py profile-all https://github.com/openreferral/hsds_example_profile --clean
```

If your profile was going to be available at `https://github.com/example-org/my-awesome-hsds-profile` then the command would be:

```
hsds_schema.py profile-all https://github.com/example-org/my-awesome-hsds-profile --clean
```

This will run the JSON Merge Patch to produce the schemas under the `schema` directory (including the `openapi.json` file!), and compile them into the `schema/compiled` directory. You should commit these files to the repo, and then they are ready to be used. It will also generate `datapackage.json` and generated examples under `examples`, which should also be committed to the repository.

### Preparing documentation

At present, producing documentation is a manual affair. We are working on integrating tools which will support you by generating some basic documentation for your Profile via [Sphinx](https://www.sphinx-doc.org/en/master/), which is compatible with [Readthedocs](https://readthedocs.org/).

Until the tooling is ready you can either document your Profile inside this README file or create your own documentation site by creating a `docs` directory and generating documentation within that.

We recommend that HSDS Profile documentation should contain at least the following:

* An overview of the Profile, its intended use-cases and audience or who may find useful
* A schema reference page containing details of each schema. This should stand on its own ie containing information about the full Profile schema once it has been merged with the HSDS Schema, not just your changes
* An API reference page with a similar scope to the above. If your Profile does not make changes to the existing HSDS API Specification, then you should explicitly state this and link to the [HSDS API Reference](http://docs.openreferral.org/en/latest/hsds/api_reference.html) as the SSOT.
* A summary of changes which your Profile makes. This can be structured however best suits your Profile and audience, but you should be clear and explicit with regards to:
  * new properties in your Profile which are not in HSDS
  * properties which your Profile removes from HSDS
  * new validation rules which your Profile adds, which are not in HSDS
  * validation rules from HSDS which your Profile removes
  * new API endpoints which are enforced by your Profile
  * any properties in HSDS which your Profile renames

## Worked Examples

This section contains some worked examples of common things you're likely going to want to do with a new HSDS Profile. Please feel free to contribute by raising a PR adding your example below.

Please note that the following examples are fairly specific and are not intended as a full tutorial for either [JSON Schema](https://json-schema.org/understanding-json-schema/index.html) or [OpenAPI](https://spec.openapis.org/oas/latest.html). You should consult the relevant materials in order to understand how to use these technologies to create the effects you desire for your Profile.

### Adding a new Field/Property to an existing Schema

This is likely one of the more common tasks of developing a new Profile. In this example, we'll be defining a new property on the [Service](http://docs.openreferral.org/en/latest/hsds/schema_reference.html#service) object.

First, let's create the file `profile/service.json` to contain our changes. This matches the name of the [service.json schema file](https://github.com/openreferral/specification/blob/3.0/schema/service.json) in HSDS.

In our purely hypothetical scenario, we're going to be adding a property which details the date of the last inspection of the service by an approved body. This is unlikely to be a real thing you'd model, but serves just to illustrate how simple this is to implement.

Inside `profile/service.json` we simply want to add to the list of properties, and include our new property:

```json
{
  "properties": {
    "last_inspected": {
      "type": "string",
      "format": "date",
      "title": "Last Inspected",
      "Description": "The date that this service was last inspected. Must be in the format YYYY-MM-DD"
    }
  }
}
```

This simply adds a new property `last_inspected` which is of a type `string` (since JSON doesn't have a built-in Date or DateTime type) but establishes that the value must be of the format `date`. Please consult the [Understanding JSON Schema](https://json-schema.org/understanding-json-schema/index.html) reference for more details on JSON Schema, if you want to add more complex properties such as those matching patterns, or entire objects.

### Make existing or new properties required

You may also want to make sure that some properties are required in your Profile. This can apply to either existing properties from the HSDS Schema which are not required in the original schema, or properties which are added by your Profile.

As before, you will need to be working inside of a file which corresponds to a schema file in HSDS. We will be adding some more requirements to the HSDS [Service](http://docs.openreferral.org/en/latest/hsds/schema_reference.html#service) schema so we will be working within `profile/service.json`, which corresponds to [service.json schema file](https://github.com/openreferral/specification/blob/3.0/schema/service.json) in HSDS.

Required properties are described using the `required` keyword in JSON Schema, which is an array of strings matching properties in the schema file. The caveat with making properties required in your Profile is that *we do not want to override the existing required array from HSDS* (at least not by accident!). To accomplish this, we use a JSON Schema trick by using the `allOf` block ([reference](https://json-schema.org/understanding-json-schema/reference/combining.html#id5)) to create an additional `required` array containing the list of our new required properties.

In the following example, we make the pre-existing `url` property of the service required in our Profile, as well as making our Profile require our new `last_inspected` property from the previous example.

Inside `profile/service.json`:

```json
{
  "properties": {
    "last_inspected": {
      "type": "string",
      "format": "date",
      "title": "Last Inspected",
      "Description": "The date that this service was last inspected. Must be in the format YYYY-MM-DD"
    }
  },
  "allOf": [
    {
      "required": [
        "url",
        "last_inspected"
      ]
    }
  ]
}
```

The `allOf` keyword sits outside of the `properties` key in the schema, because each schema has `properties` as well as a separate `required` array at the same level.

### Adding a new API Endpoint

Another common task of a Profile is to make changes to the HSDS OpenAPI specification. In this case, we'll be defining a new endpoint in the API. Please ensure you're up to speed on the [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) when making such changes yourself.

First, we create the `profile/openapi.json` file to contain our changes. This matches the name of the [openapi.json file](https://github.com/openreferral/specification/blob/3.0/schema/openapi.json) in HSDS

In our hypothetical scenario, we need to provide a new endpoint to quickly support exchanging data about organizations operating at particular locations.

Inside `profile/openapi.json` we add the endpoint with the parameter and response details as follows:

```json
{
  "paths": {
    "/organizations_at_location": {
      "get": {
        "description": "Retrieve a list of organizations operating in a location",
        "summary": "A paginated list of organizations operating in a location",
        "operationId": "getPaginatedListOfOrganizationsByLocation",
        "parameters": [
          {
            "$ref": "#/components/parameters/search"
          },
          {
            "name": "location_id",
            "in": "query",
            "required": false,
            "description": "Search for organizations by a location_id",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Retrieve paginated listings of organization that matches the location.",
            "content": {
              "application/json": {
                "schema": {
                  "properties": {
                    "contents": {
                      "type": "array",
                      "items": {
                        "$ref": "https://raw.githubusercontent.com/openreferral/specification/3.0/schema/compiled/organization.json"
                      }
                    }
                  },
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/Page"
                    }
                  ]
                }
              }
            }
          }
        }
      }
    }
  }
}
```

In this example, we add a new path which provides a GET request API endpoint. For illustrative purposes, we then define two different ways of attaching parameters to this new API endpoint.

Firstly, we provide a `search` parameter. This is re-used across a lot of the endpoints defined in the core HSDS API specification, so its details are actually stored in a `components` array elsewhere in the `openapi.json` file and can simply be referenced and re-used. You can find a list of the parameters in the `components` array starting [here](https://github.com/openreferral/specification/blob/3.0/schema/openapi.json#L542).

Secondly, we define a new parameter which is not already in the components list: `location_id`. This corresponds to the `id` property on the [location object](http://docs.openreferral.org/en/latest/hsds/schema_reference.html#location) as defined in HSDS. The parameter is defined via a [OpenAPI parameter object](https://spec.openapis.org/oas/latest.html#parameter-object).

Next, we define the `responses` for this request. We provide a response for `200`, which is a successful response and the most useful for us to define explicitly. This should be an [OpenAPI Responses object](https://spec.openapis.org/oas/latest.html#responsesObject). In our case, we are returning some JSON and actually defining a mini JSON-schema in the `schema` key, which should be used to validate the response body. Our schema is simply an array which matches the `Page` component (to enable Pagination) AND the `items` in the array reference the compiled HSDS schema for the [Organization object](http://docs.openreferral.org/en/latest/hsds/schema_reference.html#organization). If you have made changes to the `Organization` object in your Profile, you should replace this URI with a reference to the compiled schema of your Profile's `organization.json` file.

**An alternative method &ndash; editing the /organizations endpoint**

This example was chosen because, while a bit strained, it allows us to illustrate the types of things you might want to do with the API Specification for your Profile.

In some cases, you may want to limit the number of new API endpoints you introduce into your Profile's API specification and instead add functionality to an existing API endpoint.

In this example, we will achieve a similar effect to the above by adding a `location_id` parameter to the existing `/organizations` endpoint. This means we don't need to define a full [OpenAPI Path Item Object](https://spec.openapis.org/oas/latest.html#pathItemObject), and instead just add to the list of parameters.

Inside `profile/openapi.json`:

```json
{
  "paths": {
    "/organizations": {
      "get": {
        "parameters": [
          {
            "name": "location_id",
            "in": "query",
            "required": false,
            "description": "Search for organizations by a location_id",
            "schema": {
              "type": "string"
            }
          }
        ]
      }
    }
  }
}
```

This should add the `location_id` parameter from the previous example as a parameter available to the `/organizations` endpoint in your Profile. This will then be rendered correctly in e.g. a Swagger interface.

### Removing an existing Field/Property from a schema

You may want to remove some property from a schema (aka object or table). There can be many reasons for this, such as it not being relevant or possibly confusing for your use-case.

In this example, we'll be removing the `wait_time` and `fees` properties from the [Service schema](http://docs.openreferral.org/en/latest/hsds/schema_reference.html#service). These properties are deprecated in HSDS 3.0, so people should be transitioning away from using them anyway.

Since we're overriding the Service schema, we need to create `profile/service.json` if we haven't already. This matches the name of the [service.json schema file](https://github.com/openreferral/specification/blob/3.0/schema/service.json) in HSDS.

Removing properties makes use of the `null` keyword, allowing the JSON Merge Patch algorithm to patch over the definition of the property with `null`. This effectively removes the property and its validation rules from your Profile schema.

Inside `profile/service.json`:

```json
{
  "properties": {
    "wait_time": null,
    "fees": null
  }
}
```

Now we can run the HSDS Schema tools command to generate our Profile schemas and these properties will be removed from our Profile.

### Removing an existing schema ("Table" or "Object")

There may be cases where you want to remove an entire schema (object or table) from your Profile. HSDS is a permissive schema which allows people to publish additional properties not in the standard, so this will not prevent people from publishing data matching the schema or object you've removed. However, validation tools should not validate these because from the perspective of your Profile they are now additional properties rather than properties defined in your Profile.

Removing a schema works by using the `null` keyword to override the entire schema file. In this example, we're going to remove the [required_document](http://docs.openreferral.org/en/latest/hsds/schema_reference.html#required-document) schema.

Since we need to remove the entire schema file, we should create the file `profile/required_document.json`, which corresponds to the [required_document.json](https://github.com/openreferral/specification/blob/3.0/schema/required_document.json) file in the HSDS schema.

Now, we very simply put the `null` keyword as the entire contents of the file.

Inside `profile/required_document.json`:

```json
null
```

This means that, when it comes time to run the HSDS Tools and generate our Profile schemas; we should end up with a `schema/required_document.json` file containing nothing but `null`. This effectively removes the validation rules and definitions of that object from your Profile.
