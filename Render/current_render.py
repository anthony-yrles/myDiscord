from Render import render_authentication

state = render_authentication.render_main_menu()

def get_state():
    return state

def set_state(new_state):
    global state
    state = new_state