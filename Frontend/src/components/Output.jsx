import React from 'react';

const Output = ({ predictions, onClose }) => {
  if (!predictions) return null;

  const { predicted_prices } = predictions;

  const modelColors = {
    LinearRegression: 'bg-blue-500',
    DecisionTree: 'bg-green-500',
    RandomForest: 'bg-purple-500',
    GradientBoosting: 'bg-orange-500',
    SVR: 'bg-red-500'
  };

  const modelDescriptions = {
    LinearRegression: 'Linear Regression',
    DecisionTree: 'Decision Tree',
    RandomForest: 'Random Forest',
    GradientBoosting: 'Gradient Boosting',
    SVR: 'Support Vector Regression'
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-lg max-w-4xl w-full max-h-[90vh] overflow-y-auto">
        <div className="p-6">
          {/* Header */}
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-2xl font-bold text-gray-800">
              House Price Predictions
            </h2>
            <button
              onClick={onClose}
              className="text-gray-500 hover:text-gray-700 text-2xl font-bold"
            >
              ×
            </button>
          </div>

          {/* Prediction Results */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {Object.entries(predicted_prices).map(([model, price]) => (
              <div
                key={model}
                className="bg-white border border-gray-200 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 transform hover:scale-105"
              >
                <div className={`${modelColors[model]} text-white p-4 rounded-t-lg`}>
                  <h3 className="text-lg font-semibold text-center">
                    {modelDescriptions[model]}
                  </h3>
                </div>
                <div className="p-6">
                  <div className="text-center">
                    <div className="text-3xl font-bold text-gray-800 mb-2">
                      ${(price.toFixed(2) * 100000).toFixed(3)}
                    </div>
                    <div className="text-sm text-gray-600">
                      Predicted Price (in hundreds of thousands)
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>

          {/* Summary */}
          <div className="mt-6 p-4 bg-gray-50 rounded-lg">
            <h3 className="text-lg font-semibold text-gray-800 mb-2">
              Summary
            </h3>
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
              <div>
                <span className="font-medium">Highest:</span>
                <div className="text-green-600 font-bold">
                  ${Math.max(...Object.values(predicted_prices)).toFixed(2)}
                </div>
              </div>
              <div>
                <span className="font-medium">Lowest:</span>
                <div className="text-red-600 font-bold">
                  ${Math.min(...Object.values(predicted_prices)).toFixed(2)}
                </div>
              </div>
              <div>
                <span className="font-medium">Average:</span>
                <div className="text-blue-600 font-bold">
                  ${(Object.values(predicted_prices).reduce((a, b) => a + b, 0) / Object.values(predicted_prices).length).toFixed(2)}
                </div>
              </div>
              <div>
                <span className="font-medium">Range:</span>
                <div className="text-purple-600 font-bold">
                  ${(Math.max(...Object.values(predicted_prices)) - Math.min(...Object.values(predicted_prices))).toFixed(2)}
                </div>
              </div>
            </div>
          </div>

          {/* Close Button */}
          <div className="mt-6 text-center">
            <button
              onClick={onClose}
              className="bg-gray-600 text-white px-6 py-2 rounded-md hover:bg-gray-700 transition duration-200"
            >
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Output;