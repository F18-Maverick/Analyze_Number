import get_text
import interface
import search_url
import entry_space
import window_button
import download_main_func
import programme_main_loop
import filename_entry_And_writeinfile
class programe_bag:
    def __init__(self):
        self.windows=interface.window()

        self.enter_place=entry_space.enter_space(self.windows.Windows)

        self.windows_all_button=window_button.all_button(
            self.windows.Windows, self.windows.Windows_width, self.windows.Windows_height)
        self.button_display=self.windows_all_button.Windows_Button()

        self.download_Main=download_main_func.download_function(self.enter_place.entery)

        self.search_URL=search_url.search_url(self.enter_place.entery)
        self.search_openChrom=self.search_URL.search_open_chrome()

        self.get_text=get_text.get_entery_text(self.enter_place.entery)

        self.readAndwirte=filename_entry_And_writeinfile.file_name_entery(
            self.windows.computer_info_width, self.windows.computer_info_height,
            self.download_Main.file_type, self.download_Main.read_respond)
        self.filename=self.readAndwirte.filename_windows()
        self.write_in=self.readAndwirte.write_in_file()

        self.Main_loop=programme_main_loop.Main_Loop()
