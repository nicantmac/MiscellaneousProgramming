Implementing arrow key navigation in React typically involves handling keyboard events and managing the focus state of elements. You can achieve this using a custom hook or by leveraging existing libraries. 
Implementing with a Custom Hook (Manual Approach)
A common pattern is to use useEffect and useRef hooks to add a global keydown event listener and define the navigation logic within a handler function. The Roving Tabindex pattern is a recommended approach for accessibility, where only the currently focused item has a tabIndex of 0, and others have -1. 
Here is a simplified example of how to implement vertical navigation for a list:
Define a Custom Hook (e.g., useKeyboardNavigation.js): This hook manages the current active index and handles keydown events.
javascript
import { useState, useEffect, useRef } from 'react';

const useKeyboardNavigation = (itemsCount) => {
    const [activeIndex, setActiveIndex] = useState(0);
    const listRef = useRef(null);

    useEffect(() => {
        const handleKeyDown = (event) => {
            switch (event.key) {
                case 'ArrowUp':
                    event.preventDefault(); // Prevent default browser scrolling
                    setActiveIndex((prevIndex) => (prevIndex > 0 ? prevIndex - 1 : itemsCount - 1));
                    break;
                case 'ArrowDown':
                    event.preventDefault(); // Prevent default browser scrolling
                    setActiveIndex((prevIndex) => (prevIndex < itemsCount - 1 ? prevIndex + 1 : 0));
                    break;
                case 'Enter':
                    // Handle item selection (e.g., trigger a click or a function)
                    console.log(`Item ${activeIndex} selected`);
                    break;
                default:
                    break;
            }
        };

        // Attach the event listener to the window or a specific container
        // (Attaching to window for demonstration, can be more specific)
        window.addEventListener('keydown', handleKeyDown);

        return () => {
            window.removeEventListener('keydown', handleKeyDown);
        };
    }, [itemsCount, activeIndex]); // Add dependencies

    return activeIndex;
};

export default useKeyboardNavigation;
Use the Hook in your Component: Apply the activeIndex to highlight the current item and manage focus.
javascript
import React, { useRef, useEffect } from 'react';
import useKeyboardNavigation from './useKeyboardNavigation';

const MyList = ({ items }) => {
    const activeIndex = useKeyboardNavigation(items.length);
    const activeItemRef = useRef(null);

    // Ensure the active item is in view
    useEffect(() => {
        if (activeItemRef.current) {
            activeItemRef.current.focus();
        }
    }, [activeIndex]);

    return (
        <div ref={activeItemRef} tabIndex={0} style={{ outline: 'none' }}>
            {items.map((item, index) => (
                <div
                    key={index}
                    ref={index === activeIndex ? activeItemRef : null}
                    style={{
                        backgroundColor: index === activeIndex ? '#f0f0f0' : 'white',
                        padding: '10px',
                        cursor: 'pointer',
                    }}
                    tabIndex={index === activeIndex ? 0 : -1} // Roving tabindex pattern
                    onClick={() => console.log(`Clicked item ${index}`)}
                >
                    {item.name}
                </div>
            ))}
        </div>
    );
};
