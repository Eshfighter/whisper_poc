import React, { useEffect, useState } from 'react';

function TranscriptionList() {
    const [transcriptions, setTranscriptions] = useState([]);

    useEffect(() => {
        const fetchTranscriptions = async () => {
            try {
                const response = await fetch('http://localhost:8000/transcriptions');
                const data = await response.json();
                setTranscriptions(data);
            } catch (error) {
                console.error('Error fetching transcriptions:', error);
            }
        };

        fetchTranscriptions();
    }, []);

    return (
        <div>
            <h2>Transcriptions</h2>
            <ul>
                {transcriptions.map((transcription, index) => (
                    <li key={index}>
                        <strong>Filename:</strong> {transcription.filename}<br />
                        <strong>Transcription:</strong> {transcription.transcription}<br />
                        <strong>Timestamp:</strong> {transcription.timestamp}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default TranscriptionList; 