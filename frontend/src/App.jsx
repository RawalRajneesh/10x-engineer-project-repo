import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css'; // Ensure this exists for global styles
import LayoutComponent from './layouts/LayoutComponent';
import PromptList from './pages/PromptList';
import PromptDetail from './pages/PromptDetail';
import PromptCreate from './pages/PromptCreate';
import PromptEdit from './pages/PromptEdit';

function App() {
  return (
    <Router>
      <LayoutComponent>
        <Routes>
          <Route path="/" element={<PromptList />} />
          <Route path="/prompts/:id" element={<PromptDetail />} />
          <Route path="/create" element={<PromptCreate />} />
          <Route path="/edit/:id" element={<PromptEdit />} />
        </Routes>
      </LayoutComponent>
    </Router>
  );
}

export default App;
