// TodoActions.js
const actions = {
  addTodo: (text) => ({
    type: 'ADD_TODO',
    payload: text,
  }),
  toggleTodo: (id) => ({
    type: 'TOGGLE_TODO',
    payload: id,
  }),
  deleteTodo: (id) => ({
    type: 'DELETE_TODO',
    payload: id,
  }),
};

export default actions;
