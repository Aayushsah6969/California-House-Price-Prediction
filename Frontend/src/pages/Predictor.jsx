import React, { useState } from 'react';
import Form from '../components/Form';
import Output from '../components/Output';

const Predictor = () => {
  const [predictions, setPredictions] = useState(null);

  const handlePredictionResult = (result) => {
    setPredictions(result);
  };

  const handleCloseOutput = () => {
    setPredictions(null);
  };

  return (
    <div className="min-h-screen bg-gray-100 py-8">
      <div className="container mx-auto px-4">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-800 mb-4">
            California House Price Predictor
          </h1>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
            Enter the house characteristics below to get price predictions from multiple machine learning models.
            All predictions are in hundreds of thousands of dollars.
          </p>
        </div>
        
        <Form onPredictionResult={handlePredictionResult} />
        
        {predictions && (
          <Output 
            predictions={predictions} 
            onClose={handleCloseOutput} 
          />
        )}
      </div>
    </div>
  );
};

export default Predictor;