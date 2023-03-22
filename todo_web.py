import streamlit as st
import functions

todos = functions.fileread()

def add_todo():
    todo= st.session_state['add_todo'] + '\n'
    todos.append(todo)
    functions.filewrite(todos)

def complete_todo():
    todo = st.session_state[todo]
    todos.remove(todo)
    functions.filewrite(todos_arg=todos)


st.header("This is my todo app")
st.subheader("This app will make you machine")
st.text("By McMc")
st.title("Todo app")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.filewrite(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="textbox", label_visibility='hidden', on_change=add_todo, placeholder='Enter a todo', key='add_todo')
