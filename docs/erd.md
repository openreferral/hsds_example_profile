Entity Relationship Diagram
===========================

This page is an example page set up for the HSDS Example Profile. You will likely want to edit this page to make it more relevant for your profile.

Each time you build the documentation for your Profile, the tools will generate two entity relationship diagrams for your tools. The first is only for the "Core Tables", which are detailed in `core_tables.csv` file. The second is the "Full" version, containing all the tables.

These should be representative of the structure of your Profile. For example, the HSDS Example Profile removes the `Metdata` schema. If you compare the Full diagram below with the equivalent diagram [on the HSDS documentation](http://docs.openreferral.org/en/latest/hsds/logical_model.html#entity-relationship-diagram-full-version), you will see that the `metadata` table is missing (hint: it's in the top-right corner of the original).

The diagram is powered by Python code executed inside the `docs/conf.py` file, which is run every time that Sphinx builds your documentation.


## Entity Relationship Diagram (Core tables)

```{eval-rst}

`[enlarge] <./_images/entity_relationship_diagram_core_tables.svg>`_

.. raw:: html
    :file: ./extras/_images/entity_relationship_diagram_core_tables.svg
    
:download:`[download] <./extras/_images/entity_relationship_diagram_core_tables.svg>`
```

## Entity Relationship Diagram (Full)

<div style="background-color: #77DD77;">

Core tables are shown in green.

</div>

<div style="background-color: #AEC6CF;">

Other tables are shown in blue.

</div>

```{eval-rst}

`[enlarge] <./_images/entity_relationship_diagram.svg>`_

.. raw:: html
    :file: ./extras/_images/entity_relationship_diagram.svg
    
:download:`[download] <./extras/_images/entity_relationship_diagram.svg>`

```
