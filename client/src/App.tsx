import React, { useState, useEffect } from 'react';
import { FaRegThumbsDown, FaRegThumbsUp } from "react-icons/fa6";
// Followed https://stackoverflow.com/questions/57778950/how-to-load-more-search-results-when-scrolling-down-the-page-in-react-js
import InfiniteScroll from 'react-infinite-scroll-component';
import './App.css';

function App() {
  const [isLoading, setIsLoading] = useState(true);
  const [images, setImages] = useState<any[]>([]);
  const [page, setPage] = useState(1);
  const [hasMore, setHasMore] = useState(true);

  useEffect(() => {
    fetchImages();
  }, []);

  const fetchImages = async () => {
    const response = await fetch("http://localhost:5015/api/images");

    if (!response.ok) {
      throw new Error("Failed to fetch images")
    }

    const data = await response.json();
    setImages(data);
    setIsLoading(false);
  }

  const handleClick = async (thumbsUpCount: int, thumbsDownCount: int, imageId: int) => {
    //Followed https://stackoverflow.com/questions/44996357/react-fetch-post-request
    const response = await fetch("http://localhost:5015/api/react", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
      },
      body: JSON.stringify({image_id: imageId, thumbs_up: thumbsUpCount, thumbs_down: thumbsDownCount})
    });

    if (!response.ok) {
      throw new Error("Failed to update image");
    }

    fetchImages();
  }

  return (
    <div className="App">
      <InfiniteScroll dataLength={images.length} next={fetchImages} hasMore={hasMore}>
          {images.map(image => (
            <div key={image.id} className="image-container">
              <img src={image.url} className="image" alt="Gallery of photos"/>
                <div className="reactions">
                  <div className="thumbs-up">
                  <p>{image.thumbs_up}</p>
                  <FaRegThumbsUp className="thumb-icon" size={24} onClick={() => handleClick(image.thumbs_up + 1, image.thumbs_down, image.id)}/>
                </div>

                <div className="thumbs-down">
                  <p>{image.thumbs_down}</p>
                  <FaRegThumbsDown className="thumb-icon" size={24} onClick={() => handleClick(image.thumbs_up, image.thumbs_down + 1, image.id)}/>
                </div>
                </div>

            </div>
          ))}
      </InfiniteScroll>
    </div>
  );
}

export default App;
