# make imports stuff from granite easy

class Widgets:
    from gi.repository.Granite import WidgetsAboutDialog as AboutDialog
    from gi.repository.Granite import WidgetsAppMenu as AppMenu
    from gi.repository.Granite import WidgetsPopOver as PopOver
    from gi.repository.Granite import WidgetsCollapsiblePaned as CollapsiblePaned
    from gi.repository.Granite import WidgetsCompositedWindow as CompositedWindow
    from gi.repository.Granite import WidgetsDatePicker as DatePicker
    from gi.repository.Granite import WidgetsWelcome as Welcome
    from gi.repository.Granite import WidgetsPopOver as PopOver

    class CellRenderer:
        from gi.repository.Granite import WidgetsCellRendererBadge as Badge
        from gi.repository.Granite import WidgetsCellRendererExpander as Expander
