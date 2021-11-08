// import logo from './logo.svg';
import "./App.css";
import { useState, useEffect } from "react";
import Table from "react-bootstrap/Table";
import axios from "axios";

function App() {
  const [girls, setGirls] = useState([]);

  useEffect(() => {
    async function getGirls() {
      const result = await axios("http://localhost:8000/girls");
      setGirls(result.data);
    }
    getGirls();
  }, []);

  return (
    <div className="App">
      <h1>Girl's infomation</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>#</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Age</th>
          </tr>
        </thead>
        <tbody>
          {girls.map((girl) => (
            <tr key={girl.id}>
              <td>{girl.id}</td>
              <td>{girl.first_name}</td>
              <td>{girl.last_name}</td>
              <td>{girl.age}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
}

export default App;
