import { createRoot } from 'react-dom/client';  // Updated import for React 18+
import { Provider } from 'react-redux';
import store from './components/store';  // Import the Redux store
import App from './App';

// Get the root DOM node
const container = document.getElementById('root');

// Create the root for React 18
const root = createRoot(container);

// Render your app wrapped in the Redux Provider
root.render(
  <Provider store={store}>
    <App />
  </Provider>
);
