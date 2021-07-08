from datetime import datetime

from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, VSplit, Window
from prompt_toolkit.widgets import MenuContainer, MenuItem, TextArea
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.styles import Style
from prompt_toolkit.lexers import DynamicLexer, PygmentsLexer
from pygments.lexers.python import PythonLexer


# Editing area
text_field = TextArea(
    lexer=PygmentsLexer(PythonLexer),
    scrollbar=True,
    line_numbers=True,
)


def get_datetime():
    return "Opened at " + datetime.now().strftime("%d/%m/%Y, %H:%M:%S")


statusbar_field = VSplit([Window(FormattedTextControl(get_datetime()))], height=1)

# UI main body
body = HSplit([text_field, statusbar_field])

# Keybindings
bindings = KeyBindings()


@bindings.add("c-d")
def _exit(event):
    get_app().exit()


@bindings.add("c-c")
def _(event):
    ...


# Menu items
root_container = MenuContainer(
    body=body,
    menu_items=[
        MenuItem(
            "File",
            children=[
                MenuItem("New"),
                MenuItem("Save"),
                MenuItem("Exit"),
            ],
        ),
        MenuItem("View", children=[MenuItem("Status Bar")]),
        MenuItem("Info", children=[MenuItem("About")]),
    ],
    key_bindings=bindings,
)


layout = Layout(root_container, focused_element=text_field)

# Global style
style = Style.from_dict(
    {
        # empty for now
    }
)


application = Application(
    layout=layout,
    style=style,
    full_screen=True,
)


def run():
    application.run()


if __name__ == "__main__":
    run()
