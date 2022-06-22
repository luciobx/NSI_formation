import PySimpleGUI as sg
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas"\
          "vitae lectus porta, semper augue vitae, feugiat nulla. Integer "\
          " posuere diam diam, molestie ultricies nequepulvinar nec. "\
          " Vestibulum nisl sapien, tristique commodo enim a, vestibulum "\
          "rutrum elit.Morbi vestibulum pellentesque odio, eget suscipit mi"\
          " interdum a. Aliquam risus turpis, cursus id mi eu, rutrum eleifend"\
          " massa. Nullam iaculis lacus quis velit mattis molestie. Sed "\
          "condimentum pulvinar malesuada. Suspendisse congue cursus nulla, si"\
          "t amet tempus purus tempor sed. Vivamus pharetra ultricies nibh at"\
          " sodales. Donec in lacus auctor, dapibus enim sit amet, faucibus"\
          " mi. Aliquam erat volutpat."
sg.popup_scrolled(my_text, size=(50, 8))