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
├─ docs/ (A directory containing a Sphinxdoc configuration and some pages to get you started on creating documentation for your Profile. You SHOULD edit this folder manually)
├─ examples/ (A directory containing automatically generated examples. You should NOT edit this folder manually.)
├─ profile/ (The directory containing all of the changes representing your Profile. You MUST be editing files here manually.)
├─ python/ (A directory containing some Python tooling which supports generating documentation from your Profile)
├─ schema/ (A directory containing automatically generated schemas created by combining your changes in the profile directory with the HSDS Schema files. You should NOT edit this folder manually.)
├─ .readthedocs.yaml (A configuration file for a Read The Docs build to support you hosting the documentation on Read The Docs. You MAY edit this to customise your Read The Docs build.)
├─ LICENSE (The license file for this repository. The contents of the template repository are licensed by the Creative Commons Attribution Share-Alike 4.0 license. You may license your additional documentation under a different license.)
├─ README.md (This readme file! You SHOULD edit it manually once you're done with your profile, and change it to suit your needs.)
├─ core_tables.csv (A file which labels HSDS schemas as core or not. This is used to generate the ERD in the documentation, so you should NOT remove the file but you MAY edit it to define which tables are core for your Profile.)
├─ datapackage.json (An automatically generated datapackage file which will allow people to publish data using your profile in a tabular format. You should NOT edit or remove this file because it also allows the documentation tools to generate the ERD diagrams.)
```

As you can see, most of your work will be inside the `profile` directory. Most of the rest is generated and handled by the HSDS Schema tools, which you installed during the setup.

If you are producing documentation for your Profile, then you will also be doing some work inside of the `docs` directory.

### A note on the underlying technologies

HSDS 3.0 is implemented using [JSON Schema](https://json-schema.org/), while the API Specification is described using [OpenAPI](https://spec.openapis.org/) in JSON format. You will need to develop some familiarity with these technologies if you want to implement a Profile.

While the tutorials and examples in this repository aim to be clear and explain the changes that are being made to support new Profile developers who may be encountering these technologies for the first time, they are not intended as a full replacement for the relevant learning materials for either JSON Schema or OpenAPI.

Specific versions:

* HSDS 3.0 is implemented in [JSON Schema Draft 2020-12](http://json-schema.org/specification-links.html#2020-12). This was the latest version available during implementation. You do not need to declare a JSON Schema version in your Profile schema files, but you should take care not to use features that are only available in later versions of JSON Schema and be careful when using features that have a different behaviour in previous versions.
* The HSDS OpenAPI specification file is implemented in [OpenAPI version 3.1.0](https://spec.openapis.org/oas/latest.html), which was the latest version available during implementation. You should therefore ensure that any features you add to your Profile's `openapi.json` file are available in this version.

The documentation tools are based on [sphinx-doc](https://www.sphinx-doc.org/en/master/), with a default configuration compatible with [Read The Docs](https://about.readthedocs.com/). You should be at least nominally familiar with these tools if you want to get the most out of the documentation tools. If you want to use alternative tooling to generate and host documentation (e.g. Github/Gitlab pages, Hugo, Jekyll, etc.) then you can do so, but may need to generate some components separately.

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

This section contains some guidance on how to create documentation for your Profile.

This repository contains some tooling which will generate a simple documentation site template for you, using [sphinx-doc](https://www.sphinx-doc.org/en/master/). This is also configured to be compatible with [Read The Docs](https://about.readthedocs.com/). This simple site is really designed to get you started, and we intend that you make changes to the default pages.

You are not limited to the documentation tools provided here, if you prefer other documentation hosting services or documentation-generation tools.

#### What to include in Profile documentation

Regardless of whether you use this repository's documentation tools or not, a good HSDS Profiles documentation site will include the following things:

* **An overview** of the Profile explaining its intended use-cases and audience, and whoever else may find it useful.
* **A Schema Reference Page** analogous to the [HSDS Schema Reference page](https://docs.openreferral.org/en/latest/hsds/schema_reference.html). This should be self-contained and not rely on any linking out to the core HSDS docs or other Profile docs. Essentially, it should contain the entire schema reference for your Profile and not just the changes you've made. We recommend providing the reference in a tabular format. You should also consider 
* **An API Reference Page** analogous to the [HSDS API Reference page](https://docs.openreferral.org/en/latest/hsds/api_reference.html). Again, this should be self-contained and provide a thorough reference for the entire API specification in you Profile. You may want to simply generate and provide a [SwaggerUI](https://swagger.io/tools/swagger-ui/) page for this purpose, and link to this from your other documentation. Alternatively, you can generate your own API Reference Page.
* **A summary of changes** which your Profile makes to HSDS. While the Schema Reference page provides a self-contained reference page for your Profile, the summary of changes simply lists what your Profile changes from core HSDS. The motivation for this is to support data users and implementors coming from core HSDS. Providing a list or summary of these changes will make it easier for them to get started with your Profile. You should include:
  * new properties in your Profile which are not in HSDS
  * properties which your Profile removes from HSDS
  * new validation rules which your Profile adds, which are not in HSDS
  * validation rules from HSDS which your Profile removes
  * new API endpoints which are enforced by your Profile
  * any properties in HSDS which your Profile renames

#### Using the included documentation tools

As noted throughout this README, this repository provides some tools that will support you generating and maintaining documentation for your Profile. This section contains guidance on how to use the tools.

The documentation tools provide the following features:

* Sphinx-doc documentation site compatible with Read The Docs.
  * Styled for visual consistency with the HSDS documentation.
* Generates a Schema Reference page for your Profile including tabular representations of your Profile schemas.
* Generates an API Reference page for your Profile, based on your Profile's OpenAPI file.
* Generates Entity Relationship Diagrams for your Profile, with a documentation page containing them.
* Provides template pages with in-line guidance and suggestions for how to achieve advances effects.

The basic workflow of generating the documentation is as follows:

1. Edit your Profile by defining changes in the `profile/` directory, and/or write your documentation inside `docs/` directory.
2. Ensure that you've generated your Profile schemas using the HSDS Schema Tools.
3. Build your documentation locally either to check it, or for hosting elsewhere.
4. (Optional) push your changes to a repository readable by [Read The Docs](https://about.readthedocs.com/features/).

This assumes that you have done everything required in previous steps to set up the environment. If you have not done so, please go back and do this.

In general, building docs is easy and takes only a few commands. First, you will need to ensure that the Python Virtual Environment is active:

```
source .ve/bin/active
```

If you've edited your Profile schemas at all, you'll need to run the HSDS Tools to generate or update the `schema/` directory alongside `datapackage.json`.

```
hsds_schema.py profile-all https://github.com/example-org/my-awesome-hsds-profile --clean
```

You can now generate the docs locally with the following commands: 

```
cd docs/
make dirhtml
```

This will generate your docs site in `docs/_build/dirhtml`. You can use this to either inspect the docs locally, or take the generated files and host them yourself.

Alternatively, if you're using Read The Docs, you can commit and push your changes after running the HSDS Tools and then Read The Docs will build your documentation for you.

This guidance continues by describing nuances of using the documentation tools.

##### The `docs/` directory

The `docs/` directory contains most of the files needed to generate your documentation.

* `conf.py` is the main Sphinx doc configuration file and it is run every time you build your docs. The file contains the settings for setting the documentation title, as well as containing the code used to generate the ERD every time you build the docs.
* `_static/` and `_templates/` contain some custom HTML, CSS, and Javascript files used in the documentation theme. `assets/` contains other assets such as images etc.
* `extras` is a folder used as a target to generate Swagger UI files and the ERD images.

There are also some Makefiles (`make.bat` and `Makefiles`) to be compatible with build tools.

The remainder of the files are markdown files, where each file represents a page of your documentation.

The following default pages are set up for you:

* `index.md` is the landing page. You can write additional introduction copy here, and this is where you'll define what appears in the table of contents / sidebar.
* `schema_reference.md` provides the Schema Reference Page. By default it contains some in-line documentation to generate nice tabular representations of schemas, and a token for a script used to auto-generate some basic references tables.
* `api_reference.md` provides an automatically generated API reference page. By default it contains some in-line documentation on creating more advanced effects.
* `erd.md` provides a page containing the Entity Relationship Diagrams. By default it contains a brief introduction addressing you, which you should remove.
* `profile_compliance.md` provides a skeleton page designed for you to populate with details of how your Profile differs from the core HSDS.
* `changelog.md` provides a skeleton page designed for you to populate with changelog details of your Profile as it changes and grows.

We intend that you edit each of these pages to remove the default copy and tailor it to the needs of your Profile.

##### Automatically generating tabular representations of your Profile schemas

If you look at the default `docs/schema_reference.md` file, you'll notice that it contains `{{insert_schema_reference_tables}}` at the bottom.

Unlike the API Reference, which is generated via a single `openapi.json` file, the Schema Reference page will need to account for multiple different schema files in the `schema/` folder. Since your Profile may remove schemas from HSDS, this would mean that sphinx-doc would throw errors when trying to read schema files which don't exist. Alternatively, your Profile may *add* new schemas, and then the Schema Reference Page would not take these into account.

Therefore, we have included a script designed to get you started. It is really only designed to be run once to provide you with a base from which to work:

```
cd python/
./generate_schema_reference_page.py
```

This will look inside your `schema/` folder and for each schema present, will build a very basic sphinx directive adding a reference table for this schema. It will then open `docs/schema_reference.md` and replace the `{{insert_schema_reference_tables}}` token with the list of sphinx directives.

After running this, you may want to re-order the directives inside `docs/schema_reference.md` to make them appear in a more prioritised order. You can then also follow the tutorials to achieve more advanced effects.

##### Generating the API Reference

Generating the API reference is handled automatically, and depends on `schema/openapi.json` being generated by the HSDS schema tools.

The SwaggerUI version of the API Reference depends on an older version of OpenAPI (3.0, as opposed to 3.1). In the HSDS docs, the HSDS schema tools generate an OpenAPI 3.0, de-referenced, version of `schema/openapi.json` named `openapi30.json` and places it in a specific folder.

This feature is yet to be integrated into the Profiles documentation tooling, since it requires a target directory to place the generated file. We are seeking to integrate this soon.

##### Generating the ERDs

The ERDs are generated each time you build the documentation, via libraries that are stored in the repository `python/` directory, and then used in `docs/conf.py`.

The ERDs depend on `datapackage.json` to read the datapackage version of the schema, and `core_tables.csv` to recognise which ones are 'core' tables and thus change the colour of the element in the ERD.

##### Adding your own pages

You can add your own pages. Just create a markdown file where the filename represents the URL path you want for that page. For example, `taxonomy-and-classifications.md` will become `https://your-docs-site.org/en/latest/taxonomy-and-classifications`.

You can then add the page to the sidebar (referred to as the TOC tree), by editing `docs/index.md`:

``````
```{eval-rst}

.. toctree::
   :maxdepth: 1
   :caption: Reference

   schema_reference
   api_reference
   erd
   profile_compliance
   taxonomy-and-classifications  <--- your new file
   changelog

```
``````

You don't need to include the page in the TOC tree, but Sphinxdoc will warn you when it's building.

You can also rearrange the files into folders if your Profile documentation expands. For example the HSDS docs uses the following folder structure:

```
hsds/
  schema_reference.md
  api_reference.md
  etc.
initiative
  index.md
```

#### Using alternative documentation tools

You may not want to use the included documentation tooling, and there is nothing preventing you from using other tools such as a static site generator or another dedicated documentation tool.

If you do this, you will likely want to remove the documentation tools which are integrated into this repository:

* remove the contents of the `docs` directory. You may keep or remove the directory itself, depending on the workflow of the tools you're going to set up.
* remove the `.readthedocs.yaml` file, or edit it to describe a build using an alternative toolkit compatible with Read The Docs.
* remove the `python/generate_schema_reference_page.py` script, as this is designed for use with sphinx-doc.
* edit `requirements.txt` to remove references to packages designed for sphinx. These should be clearly labelled. Make sure you do not remove the hsds-schema-tools requirements!

You're then free to start integrating your own documentation tools.

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
