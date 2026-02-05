import { Loader2 } from 'lucide-react';

const Spinner = () => (
  <div className="flex items-center justify-center p-4">
    <Loader2 className="animate-spin text-blue-500" size={32} />
    <span className="ml-2 text-gray-600">Agents are working on your roadmap...</span>
  </div>
);

export default Spinner;