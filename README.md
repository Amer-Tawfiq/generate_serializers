# generate_serializers

A utility to **auto-generate Django REST Framework (DRF) serializers** for all models in specified Django apps.

---

## 🚀 Features

- Automatically creates a serializer file for each model in your Django apps.
- Saves time and avoids boilerplate code.
- Easy to integrate into any Django project.

---

## 📦 Installation

You can install the package locally:

```bash
pip install generate_serializers
pip install git+https://github.com/Amer-Tawfiq/generate_serializers.git

##   Usage Example

from generate_serializers import generate_serializers_for_apps

generate_serializers_for_apps(
    app_names=['my_app1', 'my_app2'],  # Replace with your Django app names
    project_settings_module='my_project.settings'  # Replace with your Django settings module path
)