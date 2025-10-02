import React, { useEffect, useState } from "react";

function App() {
  const [cars, setCars] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/cars/")
      .then(res => res.json())
      .then(data => setCars(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h1>Список машин</h1>
      <ul>
        {cars.map(car => (
          <li key={car.id}>{car.name} - {car.price}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
