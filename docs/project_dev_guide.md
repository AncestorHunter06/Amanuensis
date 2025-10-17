# Development Guide
## Architecture
- **src/gui/**: UI components (MainWindow, ImagePanel, TextPanel, ProjectPanel, MetadataDialog, TemplateDialog).
- **src/core/**: Business logic (ProjectManager, TemplateManager, PluginManager).
- **src/storage/**: SQLite/JSON storage for projects, metadata, templates.
- **src/plugins/**: Extensible plugins (e.g., image_filter_plugin, template_apply_plugin).
- **src/templates/**: JSON files for external templates.
