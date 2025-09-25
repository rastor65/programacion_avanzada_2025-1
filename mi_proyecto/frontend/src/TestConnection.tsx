import { useState, useEffect } from 'react';
import api from './api/client';

const TestConnection = () => {
  const [status, setStatus] = useState<string>('Probando conexión...');
  const [data, setData] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const testConnection = async () => {
      try {
        // Probar endpoint de Swagger (siempre disponible)
        const response = await api.get('/swagger/');
        setStatus('✅ Conexión exitosa!');
        setData({ 
          message: 'Conexión establecida correctamente',
          endpoint: '/swagger/',
          status: response.status 
        });
        setError(null);
      } catch (err: any) {
        if (err.response) {
          // El servidor respondió pero con error
          if (err.response.status === 404) {
            setStatus('⚠️ Servidor respondió pero endpoint no encontrado');
            setError(`Error 404: El endpoint no existe. Esto es normal si no tienes Swagger configurado.`);
            setData({ 
              message: 'El servidor Django está funcionando, pero el endpoint específico no existe',
              status: err.response.status 
            });
          } else {
            setStatus('⚠️ Servidor respondió pero con error');
            setError(`Error ${err.response.status}: ${err.response.statusText}`);
            setData(err.response.data);
          }
        } else if (err.request) {
          // No se pudo conectar al servidor
          setStatus('❌ No se pudo conectar al servidor');
          setError('Verifica que el backend esté corriendo en http://localhost:8000');
        } else {
          setStatus('❌ Error inesperado');
          setError(err.message);
        }
      }
    };

    testConnection();
  }, []);

  return (
    <div className="p-6 max-w-2xl mx-auto bg-white rounded-lg shadow-lg">
      <h2 className="text-2xl font-bold mb-4 text-gray-800">Prueba de Conexión React ↔ Django</h2>
      
      <div className="mb-4">
        <p className="text-lg font-semibold">{status}</p>
      </div>

      {error && (
        <div className="mb-4 p-4 bg-red-100 border border-red-400 text-red-700 rounded">
          <p className="font-semibold">Error:</p>
          <p>{error}</p>
        </div>
      )}

      {data && (
        <div className="mb-4 p-4 bg-green-100 border border-green-400 text-green-700 rounded">
          <p className="font-semibold">Datos recibidos:</p>
          <pre className="mt-2 text-sm overflow-auto">
            {JSON.stringify(data, null, 2)}
          </pre>
        </div>
      )}

      <div className="text-sm text-gray-600">
        <p><strong>Backend:</strong> http://localhost:8000</p>
        <p><strong>Frontend:</strong> http://localhost:5173</p>
        <p><strong>Endpoint probado:</strong> /swagger/</p>
        <p><strong>Estado:</strong> {status}</p>
      </div>
    </div>
  );
};

export default TestConnection;
