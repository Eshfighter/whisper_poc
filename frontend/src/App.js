import React from 'react';
import './App.css';
import FileUpload from './components/FileUpload';
import TranscriptionList from './components/TranscriptionList';
import SearchTranscriptions from './components/SearchTranscriptions';

function App() {
  return (
    <div className="App">
      <h1>Audio Transcription Service</h1>
      <FileUpload />
      <TranscriptionList />
      <SearchTranscriptions />
    </div>
  );
}

export default App;
