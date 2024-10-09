import { useSelector, useDispatch } from 'react-redux';

const App = () => {
  // Access Redux state
  const counter = useSelector((state) => state.counter);
  // Get the dispatch function
  const dispatch = useDispatch();

  return (
    <div style={{ textAlign: 'center' }}>
      <h1>Redux Counter</h1>
      <h2>Counter: {counter}</h2>
      <button onClick={() => dispatch({ type: 'INCREMENT' })}>Increment</button>
      <button onClick={() => dispatch({ type: 'DECREMENT' })}>Decrement</button>
    </div>
  );
};

export default App;
