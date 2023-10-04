"""
Authors: BW, EL, CC, JP

Purpose: Main entry point of application.
"""

from dearpygui.dearpygui import *

def init():
   create_context()
   create_viewport()
   setup_dearpygui()

   with window(label = "test window"):
      add_text("Sliders and stuff")
      add_slider_float(label= float,min_value=1.0, max_value=25.0)

   show_viewport()
   start_dearpygui()
   destroy_context()


if __name__ == "__main__":
   init()