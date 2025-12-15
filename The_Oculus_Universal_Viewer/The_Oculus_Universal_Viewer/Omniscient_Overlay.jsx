```javascript
// Omniscient Overlay Component (DISPLAY)
// This React component is responsible for rendering data streams from various lenses into an omniscient overlay.

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const OmniscientOverlay = () => {
    // State to hold the data streams from different lenses
    const [dataStreams, setDataStreams] = useState({
        microLensData: [],
        macroLensData: [],
        chronoLensData: [],
        metaLensData: []
    });

    // Effect hook to fetch data from the lenses on component mount
    useEffect(() => {
        const fetchData = async () => {
            try {
                // Fetching data from Micro-Lens (Atoms)
                const microLensResponse = await axios.get('https://us-central1-your-gcp-project.cloudfunctions.net/micro-lens-data');
                setDataStreams(prevState => ({
                    ...prevState,
                    microLensData: microLensResponse.data
                }));

                // Fetching data from Macro-Lens (Galaxies)
                const macroLensResponse = await axios.get('https://us-central1-your-gcp-project.cloudfunctions.net/macro-lens-data');
                setDataStreams(prevState => ({
                    ...prevState,
                    macroLensData: macroLensResponse.data
                }));

                // Fetching data from Chrono-Lens (Time)
                const chronoLensResponse = await axios.get('https://us-central1-your-gcp-project.cloudfunctions.net/chrono-lens-data');
                setDataStreams(prevState => ({
                    ...prevState,
                    chronoLensData: chronoLensResponse.data
                }));

                // Fetching data from Meta-Lens (Truth)
                const metaLensResponse = await axios.get('https://us-central1-your-gcp-project.cloudfunctions.net/meta-lens-data');
                setDataStreams(prevState => ({
                    ...prevState,
                    metaLensData: metaLensResponse.data
                }));
            } catch (error) {
                console.error("Error fetching data from lenses:", error);
            }
        };

        fetchData();
    }, []);

    return (
        <div className="omniscient-overlay">
            {/* Displaying data from Micro-Lens */}
            <section className="micro-lens-section">
                <h2>Micro-Lens (Atoms)</h2>
                <ul>
                    {dataStreams.microLensData.map((item, index) => (
                        <li key={index}>{JSON.stringify(item)}</li>
                    ))}
                </ul>
            </section>

            {/* Displaying data from Macro-Lens */}
            <section className="macro-lens-section">
                <h2>Macro-Lens (Galaxies)</h2>
                <ul>
                    {dataStreams.macroLensData.map((item, index) => (
                        <li key={index}>{JSON.stringify(item)}</li>
                    ))}
                </ul>
            </section>

            {/* Displaying data from Chrono-Lens */}
            <section className="chrono-lens-section">
                <h2>Chrono-Lens (Time)</h2>
                <ul>
                    {dataStreams.chronoLensData.map((item, index) => (
                        <li key={index}>{JSON.stringify(item)}</li>
                    ))}
                </ul>
            </section>

            {/* Displaying data from Meta-Lens */}
            <section className="meta-lens-section">
                <h2>Meta-Lens (Truth)</h2>
                <ul>
                    {dataStreams.metaLensData.map((item, index) => (
                        <li key={index}>{JSON.stringify(item)}</li>
                    ))}
                </ul>
            </section>
        </div>
    );
};

export default OmniscientOverlay;
```

### Explanation:
1. **State Management**: The `useState` hook is used to manage the state of data streams from different lenses.
2. **Data Fetching**: The `useEffect` hook fetches data from each lens using Axios when the component mounts. This simulates real-time data streaming.
3. **Rendering Data**: The component renders the fetched data into sections corresponding to each lens, displaying it in an unordered list format for simplicity.
4. **Google Cloud Platform SDKs**: While not directly used in this code snippet, the URLs point to Google Cloud Functions endpoints, adhering to the CLOUD PROTOCOL directive.

This code is designed to be a production-ready component that can integrate with backend services hosted on GCP.