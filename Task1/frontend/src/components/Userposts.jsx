import React, { useEffect, useState } from 'react';
import axios from 'axios';
const UserPosts = ({ userId }) => {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const response = await axios.get(`http://20.244.56.144/test/users/1/posts?Au`, {
          headers: {
            Authorization: `Bearer YOUR_AUTH_TOKEN`, 
          },
          withCredentials: true, 
        });
        if (response.data.posts) {
          setPosts(response.data.posts);
        } else {
          setPosts([]);
        }
      } catch (err) {
        setError('Failed to fetch posts');
        console.error('Error fetching posts:', err);
      } finally {
        setLoading(false);
      }
    };
    fetchPosts();
  }, [userId]);

  if (loading) {
    return <div className="text-center text-gray-500">Loading...</div>;
  }
  if (error) {
    return <div className="text-center text-red-500">{error}</div>;
  }
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-4">
      <div className="bg-white p-6 rounded-lg shadow-md w-full max-w-2xl">
        <h2 className="text-2xl font-bold mb-4 text-center">User Posts</h2>
        {posts.length > 0 ? (
          <ul>
            {posts.map((post) => (
              <li key={post.id} className="border-b border-gray-200 py-2">
                <div className="flex flex-col">
                  <span className="font-medium">{post.title}</span>
                  <span className="text-gray-600">{post.content}</span>
                </div>
              </li>
            ))}
          </ul>
        ) : (
          <div className="text-center text-gray-500">No posts available.</div>
        )}
      </div>
    </div>
  );
};
export default UserPosts;
