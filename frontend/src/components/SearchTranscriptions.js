import React, { useState } from 'react';

function SearchTranscriptions() {
    const [searchTerm, setSearchTerm] = useState('');
    const [searchResults, setSearchResults] = useState([]);

    const handleSearch = async () => {
        try {
            const response = await fetch(`http://localhost:8000/search?filename=${searchTerm}`);
            const data = await response.json();
            setSearchResults(data);
        } catch (error) {
            console.error('Error searching transcriptions:', error);
        }
    };

    return (
        <div>
            <h2>Search Transcriptions</h2>
            <input
                type="text"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                placeholder="Enter filename"
            />
            <button onClick={handleSearch}>Search</button>
            <ul>
                {searchResults.map((result, index) => (
                    <li key={index}>
                        <strong>Filename:</strong> {result.filename}<br />
                        <strong>Transcription:</strong> {result.transcription}<br />
                        <strong>Timestamp:</strong> {result.timestamp}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default SearchTranscriptions; 