import React, {useState, useEffect} from "react";
import axios from "axios"

function RestAPI(){
    const [posts ,setPosts] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/rest/post/")
            .then(response => {
            setPosts(response.data);
            })
            .catch(error => {
            console.error('There was an error!', error);
            });
    }, []);
    
    return (
        <section className="content-list">
            <ul>
                {posts.map(post => (
                    <li className="content-item" key={post.id}>
                        <h2 className="content-item__title">{post.title}</h2>
                        <div className="content-details">
                            <div className="company">
                                <span>{post.company}</span>
                            </div>
                            <div className="date-views-likes">
                                <span>{new Date(post.date).toLocaleDateString()}</span>
                            </div>
                        </div>
                        <a href={post.url}>Link</a>
                    </li>
                ))}
            </ul>
        </section>
    );

}

export default RestAPI;