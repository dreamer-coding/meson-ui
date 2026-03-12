#
# ==============================================================================
# Author: Michael Gene Brockus (Dreamer)
# Email: michaelbrockus@gmail.com
# Organization: Fossil Logic
# Description:
#     This file is part of the Fossil Logic project, where innovation meets
#     excellence in software development. Michael Gene Brockus, also known as
#     "Dreamer," is a dedicated contributor to this project. For any inquiries,
#     feel free to contact Michael at michaelbrockus@gmail.com.
# ==============================================================================
#
from tkinter.scrolledtext import ScrolledText
import tkinter.ttk as ttk
import tkinter as tk
import webbrowser
import threading
import os

from .mesonbuild import MesonBuild
from .appinfo import AppInfo, AppThemes
from .dialog.subprojects import SubprojectsDialog
from .dialog.configure import ConfigureDialog
from .dialog.tutorial import TutorialDialog
from .dialog.setup import SetupDialog
from .dialog.init import InitDialog


class MesonBuildGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Meson Build GUI")
        self.root.geometry("660x400")
        self.root.resizable(False, False)

        self.app_info = AppInfo()
        self.apply_styles()
        self.create_widgets()
        self.apply_theme()

        self.meson_build = MesonBuild(
            self.source_dir_entry.get(), self.build_dir_entry.get()
        )

    def apply_styles(self):
        self.style = ttk.Style()
        self.style.configure(
            "Blue.TButton",
            foreground="black",
            background="#ADD8E6",
            font=("Helvetica", 10, "bold"),
        )

    def create_widgets(self):
        self.create_menu()

        self.setup_button = ttk.Button(
            self.root,
            text="Setup",
            command=self.setup_project,
            style="Blue.TButton"
        )
        self.configure_button = ttk.Button(
            self.root,
            text="Configure",
            command=self.configure_project,
            style="Blue.TButton",
        )
        self.compile_button = ttk.Button(
            self.root,
            text="Compile",
            command=self.compile_project,
            style="Blue.TButton",
        )
        self.test_button = ttk.Button(
            self.root, text="Test", command=self.test_project, style="Blue.TButton"
        )
        self.install_button = ttk.Button(
            self.root,
            text="Install",
            command=self.install_project,
            style="Blue.TButton",
        )
        self.version_button = ttk.Button(
            self.root, text="Version", command=self.show_version, style="Blue.TButton"
        )
        self.introspect_button = ttk.Button(
            self.root,
            text="Introspection",
            command=self.show_introspection,
            style="Blue.TButton",
        )
        self.clear_terminal_button = ttk.Button(
            self.root,
            text="Clear Terminal",
            command=self.clear_terminal,
            style="Blue.TButton",
        )
        self.tool_info_button = ttk.Button(
            self.root,
            text="Tool Info",
            command=self.get_tool_info,
            style="Blue.TButton",
        )
        self.tutorial_button = ttk.Button(
            self.root, text="Tutorial", command=self.show_tutorial, style="Blue.TButton"
        )

        self.source_dir_label = ttk.Label(
            self.root,
            text="Source Directory:",
            background="dark gray",
            font=("Helvetica", 10, "bold"),
        )
        self.source_dir_entry = ttk.Entry(self.root, width=50)
        self.source_dir_entry.insert(0, os.getcwd())
        self.source_dir_button = ttk.Button(
            self.root,
            text="Browse",
            command=self.browse_source_dir,
            style="Blue.TButton",
        )

        self.build_dir_label = ttk.Label(
            self.root,
            text="Build Directory:",
            background="dark gray",
            font=("Helvetica", 10, "bold"),
        )
        self.build_dir_entry = ttk.Entry(self.root, width=50)
        self.build_dir_entry.insert(0, "builddir")
        self.clear_paths_button = ttk.Button(
            self.root,
            text="Clear Paths",
            command=self.clear_paths,
            style="Blue.TButton",
        )

        self.terminal = ScrolledText(
            self.root,
            height=10,
            state=tk.DISABLED,
            wrap=tk.WORD,
            background="black",
            foreground="white",
            font="helvetica 10 bold",
        )

        row1_buttons = [
            self.setup_button,
            self.configure_button,
            self.compile_button,
            self.test_button,
            self.install_button
        ]

        for col, button in enumerate(row1_buttons):
            button.grid(row=0, column=col, pady=10, padx=10, sticky=tk.W + tk.E)

        self.source_dir_label.grid(row=1, column=0, pady=5, padx=10, sticky=tk.W)
        self.source_dir_entry.grid(
            row=1, column=1, pady=5, padx=10, sticky=tk.W + tk.E, columnspan=3
        )
        self.source_dir_button.grid(
            row=1, column=4, pady=5, padx=10, sticky=tk.W + tk.E
        )

        self.build_dir_label.grid(row=2, column=0, pady=5, padx=10, sticky=tk.W)
        self.build_dir_entry.grid(
            row=2, column=1, pady=5, padx=10, sticky=tk.W + tk.E, columnspan=3
        )
        self.clear_paths_button.grid(
            row=2, column=4, pady=5, padx=10, sticky=tk.W + tk.E
        )

        self.terminal.grid(
            row=3,
            column=0,
            columnspan=5,
            pady=10,
            padx=10,
            sticky=tk.W + tk.E + tk.N + tk.S,
        )

        row2_buttons = [
            self.version_button,
            self.introspect_button,
            self.clear_terminal_button,
            self.tool_info_button,
            self.tutorial_button,
        ]

        for col, button in enumerate(row2_buttons):
            button.grid(row=4, column=col, pady=10, padx=10, sticky=tk.W + tk.E)

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        options_menu = tk.Menu(menubar, tearoff=0)
        options_menu.add_command(label="Tutorial", command=self.show_tutorial)
        options_menu.add_command(label="Version", command=self.show_version)
        options_menu.add_command(label="Clear Terminal", command=self.clear_terminal)
        options_menu.add_command(label="Help", command=self.get_tool_info)
        menubar.add_cascade(label="Options", menu=options_menu)

        actions_menu = tk.Menu(menubar, tearoff=0)
        actions_menu.add_command(label="Setup", command=self.setup_project)
        actions_menu.add_command(label="Configure", command=self.configure_project)
        actions_menu.add_command(label="Compile", command=self.compile_project)
        actions_menu.add_command(label="Test", command=self.test_project)
        actions_menu.add_command(label="Introspection", command=self.show_introspection)
        actions_menu.add_command(label="Install", command=self.install_project)
        actions_menu.add_command(label="Init", command=self.init_project)
        actions_menu.add_command(label="Subprojects", command=self.manage_subprojects)
        menubar.add_cascade(label="Actions", menu=actions_menu)

        support_menu = tk.Menu(menubar, tearoff=0)
        support_menu.add_command(
            label="Meson Website",
            command=lambda: self.open_url("https://mesonbuild.com/"),
        )
        support_menu.add_command(
            label="Documentation",
            command=lambda: self.open_url(
                "https://fossillogic.com/docs/meson-ui-overview"
            ),
        )
        support_menu.add_command(
            label="Repository",
            command=lambda: self.open_url("https://github.com/fossillogic/meson-ui"),
        )
        support_menu.add_command(
            label="Report Issue",
            command=lambda: self.open_url(
                "https://github.com/fossillogic/meson-ui/issues"
            ),
        )
        menubar.add_cascade(label="Support", menu=support_menu)

    def open_url(self, url):
        webbrowser.open(url)

    def apply_theme(self):
        meson_teal = "#4f5253"
        dark_bg = "#1e1e1e"
        light_text = "#e0e0e0"
        
        self.root.configure(bg=dark_bg)
        self.source_dir_label.configure(background=dark_bg, foreground=light_text)
        self.build_dir_label.configure(background=dark_bg, foreground=light_text)
        self.terminal.configure(background="#0d0d0d", foreground="#237bff")
        self.style.configure(
            "Blue.TButton", background=meson_teal, foreground="white"
        )

    def browse_source_dir(self):
        try:
            directory = tk.filedialog.askdirectory()
            if directory:
                self.source_dir_entry.delete(0, tk.END)
                self.source_dir_entry.insert(0, directory)
                self.build_dir_entry.delete(0, tk.END)
                self.build_dir_entry.insert(0, os.path.join(directory, "builddir"))
                self.meson_build.source_dir = directory
                self.meson_build.build_dir = os.path.join(directory, "builddir")
        except Exception as e:
            tk.messagebox.showerror("Browse Directory Error", f"Failed to browse directory: {str(e)}")

    def clear_paths(self):
        try:
            self.source_dir_entry.delete(0, tk.END)
            self.build_dir_entry.delete(0, tk.END)
        except Exception as e:
            tk.messagebox.showerror("Clear Paths Error", f"Failed to clear paths: {str(e)}")

    def validate_directory(self, directory):
        if not os.path.isdir(directory):
            tk.messagebox.showerror("Invalid Directory", f"Directory '{directory}' does not exist. Please check the path and try again.")
            return False
        return True

    def update_terminal(self, message):
        self.terminal.configure(state=tk.NORMAL)
        self.terminal.insert(tk.END, message + "\n")
        self.terminal.see(tk.END)
        self.terminal.update()
        self.terminal.configure(state=tk.DISABLED)

    def setup_project(self):
        try:
            build_dir = self.build_dir_entry.get()
            if not build_dir or not self.validate_directory(os.path.dirname(build_dir) or "."):
                return
            result = SetupDialog(self.root, self.apply_theme).result
            if result is None:
                return
            build_dir, other_options = result
            self.build_dir_entry.delete(0, tk.END)
            self.build_dir_entry.insert(0, build_dir)
            threading.Thread(
                target=self.run_setup_thread, args=(build_dir, other_options), daemon=True
            ).start()
        except Exception as e:
            tk.messagebox.showerror("Setup Error", f"Failed to initialize project setup: {str(e)}")

    def run_setup_thread(self, build_dir, other_options):
        try:
            self.meson_build.source_dir = self.source_dir_entry.get()
            self.meson_build.build_dir = build_dir
            self.update_terminal(f"Setting up the project in {build_dir}...\n")
            output = self.meson_build.setup(other_options)
            self.update_terminal(output)
        except Exception as e:
            self.update_terminal(f"Setup Error: Failed to set up project - {str(e)}")

    def configure_project(self):
        try:
            build_dir = self.build_dir_entry.get()
            if not build_dir or not self.validate_directory(build_dir):
                return
            result = ConfigureDialog(self.root, self.apply_theme).result
            if result is None:
                return
            build_dir, other_options = result
            threading.Thread(
                target=self.run_configure_thread, args=(build_dir, other_options), daemon=True
            ).start()
        except Exception as e:
            tk.messagebox.showerror("Configure Error", f"Failed to initialize project configuration: {str(e)}")

    def run_configure_thread(self, build_dir, other_options):
        try:
            self.meson_build.build_dir = build_dir
            self.update_terminal(f"Configuring the project in {build_dir}...\n")
            output = self.meson_build.configure(other_options)
            self.update_terminal(output)
        except Exception as e:
            self.update_terminal(f"Configure Error: Failed to configure project - {str(e)}")

    def compile_project(self):
        try:
            build_dir = self.build_dir_entry.get()
            if not build_dir or not self.validate_directory(build_dir):
                return
            self.update_terminal("Compiling the project...\n")
            threading.Thread(target=self.run_compile_thread, daemon=True).start()
        except Exception as e:
            tk.messagebox.showerror("Compile Error", f"Failed to initialize project compilation: {str(e)}")

    def run_compile_thread(self):
        try:
            build_dir = self.build_dir_entry.get()
            self.meson_build.build_dir = build_dir
            output = self.meson_build.compile()
            self.update_terminal(output)
        except Exception as e:
            self.update_terminal(f"Compile Error: Compilation failed - {str(e)}")

    def test_project(self):
        try:
            build_dir = self.build_dir_entry.get()
            if not build_dir or not self.validate_directory(build_dir):
                return
            self.update_terminal("Testing the project...\n")
            threading.Thread(target=self.run_test_thread, daemon=True).start()
        except Exception as e:
            tk.messagebox.showerror("Test Error", f"Failed to initialize project testing: {str(e)}")

    def run_test_thread(self):
        try:
            build_dir = self.build_dir_entry.get()
            self.meson_build.build_dir = build_dir
            output = self.meson_build.test()
            self.update_terminal(output)
        except Exception as e:
            self.update_terminal(f"Test Error: Testing failed - {str(e)}")

    def install_project(self):
        try:
            build_dir = self.build_dir_entry.get()
            if not build_dir or not self.validate_directory(build_dir):
                return
            self.update_terminal("Installing the project...\n")
            threading.Thread(target=self.run_install_thread, daemon=True).start()
        except Exception as e:
            tk.messagebox.showerror("Install Error", f"Failed to initialize project installation: {str(e)}")

    def run_install_thread(self):
        try:
            build_dir = self.build_dir_entry.get()
            self.meson_build.build_dir = build_dir
            output = self.meson_build.install()
            self.update_terminal(output)
        except Exception as e:
            self.update_terminal(f"Install Error: Installation failed - {str(e)}")

    def show_version(self):
        try:
            self.update_terminal("Meson Version:\n")
            threading.Thread(target=self.run_version_thread, daemon=True).start()
        except Exception as e:
            tk.messagebox.showerror("Version Error", f"Failed to retrieve Meson version: {str(e)}")

    def run_version_thread(self):
        try:
            output = self.meson_build.run_command(["meson", "--version"])
            self.update_terminal(output)
        except Exception as e:
            self.update_terminal(f"Version Error: Failed to get Meson version - {str(e)}")

    def show_introspection(self):
        try:
            build_dir = self.build_dir_entry.get()
            if not build_dir or not self.validate_directory(build_dir):
                return
            self.update_terminal(f"Introspecting build directory {build_dir}...\n")
            threading.Thread(target=self.run_introspection_thread, daemon=True).start()
        except Exception as e:
            tk.messagebox.showerror("Introspection Error", f"Failed to initialize introspection: {str(e)}")

    def run_introspection_thread(self):
        try:
            build_dir = self.build_dir_entry.get()
            self.meson_build.build_dir = build_dir
            output = self.meson_build.introspect()
            self.update_terminal(output)
        except Exception as e:
            self.update_terminal(f"Introspection Error: Failed to introspect build - {str(e)}")

    def clear_terminal(self):
        try:
            self.terminal.configure(state=tk.NORMAL)
            self.terminal.delete("1.0", tk.END)
            self.terminal.configure(state=tk.DISABLED)
        except Exception as e:
            tk.messagebox.showerror("Clear Terminal Error", f"Failed to clear terminal: {str(e)}")

    def get_tool_info(self):
        try:
            self.update_terminal("Meson Build GUI Information:\n")
            threading.Thread(target=self.run_tool_info_thread, daemon=True).start()
        except Exception as e:
            tk.messagebox.showerror("Tool Info Error", f"Failed to retrieve tool information: {str(e)}")

    def run_tool_info_thread(self):
        try:
            self.update_terminal(
                "This tool assists in building Meson projects using a graphical user interface.\n"
            )
            self.update_terminal(
                "It provides options to set up, compile, test, install, and get information about the Meson project.\n"
            )
            self.update_terminal(
                f"Created by {self.app_info.author}, lead developer at Fossil Logic.\n"
            )
        except Exception as e:
            self.update_terminal(f"Tool Info Error: Failed to display information - {str(e)}")

    def show_tutorial(self):
        try:
            TutorialDialog(self.root, self.apply_theme)
        except Exception as e:
            tk.messagebox.showerror("Tutorial Error", f"Failed to open tutorial dialog: {str(e)}")

    def init_project(self):
        try:
            result = InitDialog(self.root, self.apply_theme).result
            if result is None:
                return
            project_name, language, other_options = result
            self.update_terminal(f"Initializing the project {project_name}...\n")
            threading.Thread(
                target=self.run_init_thread, args=(project_name, language, other_options), daemon=True
            ).start()
        except Exception as e:
            tk.messagebox.showerror("Init Error", f"Failed to initialize project: {str(e)}")

    def run_init_thread(self, project_name, language, other_options):
        try:
            output = self.meson_build.init(f"--name {project_name} --language {language} {other_options}")
            self.update_terminal(output)
        except Exception as e:
            self.update_terminal(f"Init Error: Project initialization failed - {str(e)}")

    def manage_subprojects(self):
        try:
            SubprojectsDialog(self.root, self.apply_theme)
        except Exception as e:
            tk.messagebox.showerror("Subprojects Error", f"Failed to open subprojects dialog: {str(e)}")


def main():
    root = tk.Tk()
    MesonBuildGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
