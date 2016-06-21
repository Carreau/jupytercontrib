{% extends "markdown.tpl" %}

{% block input %}
{% if nb.metadata.language_info %}
{```{ nb.metadata.language_info.name }}
{% else %}
```python
{% endif %}{{ cell.source}}
```
{% endblock input %}

{% block traceback_line %}
```output
{{ line.rstrip() | strip_ansi }}
```
{% endblock traceback_line %}

{% block stream %}
```output
{{ output.text.rstrip() }}
```
{% endblock stream %}

{% block data_text scoped %}
```output
{{ output.data['text/plain'].rstrip() }}
```
{% endblock data_text %}
