import { useState } from "react";
import { FiPlusSquare } from "react-icons/fi";

const MAX_HEATING = 8;
const URL = "http://localhost:5000/";

function App() {
  const [name, setName] = useState("");
  const [pinValues, setPinValues] = useState({} as Record<string, boolean>);

  const hasChanges = Object.keys(pinValues).length > 0;
  const isPinActive = (id: number, currentValue: boolean) => {
    if (id in pinValues) {
      return pinValues[id];
    }

    return currentValue;
  };

  const pins = new Array(MAX_HEATING).fill(false).map((v, i) => (
    <button
      onClick={() => setPinValues({ ...pinValues, [i]: !v })}
      className={`px-4 py-2 rounded-md border-slate-600 border ${
        isPinActive(i, v) ? "bg-slate-200" : "opacity-50"
      }`}
    >
      {i + 1}
    </button>
  ));

  const submitChanges = () => {
    console.log(pinValues);
  };

  return (
    <div className="p-4">
      <div className="flex gap-4">
        <div className="flex gap-4">{pins}</div>
        <button
          onClick={() => submitChanges()}
          className="bg-slate-400 px-2 rounded disabled:bg-slate-200 disabled:text-slate-400"
          disabled={!hasChanges}
        >
          Submit
        </button>
      </div>
    </div>
  );
}

export default App;
