import { useState } from 'react';
import axios from 'axios';

// 1. Keep the function logic
const useRoadmap = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const generateRoadmap = async (githubUsername) => {
    setLoading(true);
    setError(null);
    try {
      // Use the environment variable for the backend URL
      const response = await axios.post(`http://127.0.0.1:8000/generate-roadmap`, {
        user_id: "saad_22f3411", 
        github_username: githubUsername
      });
      setData(response.data.data);
    } catch (err) {
      setError(err.response?.data?.detail || "Failed to generate roadmap.");
    } finally {
      setLoading(false);
    }
  };

  return { data, loading, error, generateRoadmap };
};

// 2. Add this line at the very bottom!
export default useRoadmap;