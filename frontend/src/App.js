import React from 'react';
import QrReader from 'react-qr-reader';
import axios from './services/api';

function App() {
  const [codigo, setCodigo] = React.useState(null);
  const [dados, setDados] = React.useState(null);

  const handleScan = (data) => {
    if (data) {
      setCodigo(data);
      axios.get(`/consulta?codigo=${data}`).then(res => setDados(res.data));
    }
  };

  return (
    <div>
      <h2>Leitor de Documentos Fiscais</h2>
      {!codigo && <QrReader onScan={handleScan} onError={err => console.error(err)} />}
      {dados && <button onClick={() => axios.post("/exportar", dados)}>Exportar para Excel</button>}
    </div>
  );
}

export default App;
