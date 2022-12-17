import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      hey
      <h3>{process.env.NODE_ENV}</h3>
      <img src="/logo192.png" alt="" />
      <img src={logo} alt="" />
    </div>
  );
}

export default App;
