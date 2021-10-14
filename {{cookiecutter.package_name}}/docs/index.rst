{{ cookiecutter.project_name }}
{% set heading_length = cookiecutter.project_name | length -%}
{{ "=" * heading_length }}

Contents
========

.. toctree::
   :maxdepth: 3

   API Reference <api_reference/index>
