import subprocess


def copy_to_clipboard_on_mac(text):
    process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(text.encode('utf-8'))

def copy_to_clipboard_on_linux(text):
    subprocess.run(['echo', '-n', text], stdout=subprocess.PIPE)
    subprocess.run(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
