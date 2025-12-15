// User Perception Component (ID: EYE)
// This component is responsible for capturing and processing user interactions and perceptions.
// It serves as the entry point for all data streams in The_Oculus_Universal_Viewer.

import React, { useState, useEffect } from 'react';
// Replaced cloud-only SDK with lightweight local dispatch via fetch

const UserPerception = () => {
    const [userInput, setUserInput] = useState('');
    const [zoomLevel, setZoomLevel] = useState('default'); // default, micro, macro
    const [timeControl, setTimeControl] = useState('present'); // past, present, future
    const [truthRevealed, setTruthRevealed] = useState(false);

    useEffect(() => {
        let aborted = false;
        const controller = new AbortController();

        const send = async (endpoint, payload) => {
            try {
                await fetch(endpoint, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload),
                    signal: controller.signal,
                });
            } catch (err) {
                // Non-fatal in dev environments without backend
                console.warn('Dispatch failed (non-fatal):', err);
            }
        };

        // Debounce a bit to avoid spamming on rapid UI changes
        const t = setTimeout(() => {
            if (aborted) return;
            const payload = { userInput, zoomLevel, timeControl, truthRevealed, ts: Date.now() };

            if (zoomLevel === 'micro') {
                send('/api/lens/micro', payload);
            } else if (zoomLevel === 'macro') {
                send('/api/lens/macro', payload);
            }

            if (timeControl !== 'present') {
                send('/api/lens/chrono', payload);
            }

            if (truthRevealed) {
                send('/api/lens/meta', payload);
            }
        }, 150);

        return () => {
            aborted = true;
            controller.abort();
            clearTimeout(t);
        };
    }, [userInput, zoomLevel, timeControl, truthRevealed]);

    const handleUserInput = (event) => {
        setUserInput(event.target.value);
    };

    const handleZoomIn = () => {
        setZoomLevel('micro');
    };

    const handleZoomOut = () => {
        setZoomLevel('macro');
    };

    const handleRewind = () => {
        setTimeControl('past');
    };

    const handleFastForward = () => {
        setTimeControl('future');
    };

    const handleRevealIntent = () => {
        setTruthRevealed(true);
    };

    return (
        <div className="user-perception">
            <input
                type="text"
                value={userInput}
                onChange={handleUserInput}
                placeholder="Enter your perception..."
            />
            <button onClick={handleZoomIn}>Zoom In</button>
            <button onClick={handleZoomOut}>Zoom Out</button>
            <button onClick={handleRewind}>Rewind</button>
            <button onClick={handleFastForward}>Fast Forward</button>
            <button onClick={handleRevealIntent}>Reveal Intent</button>
        </div>
    );
};

export default UserPerception;
