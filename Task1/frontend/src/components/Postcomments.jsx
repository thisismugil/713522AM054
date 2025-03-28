import React, { useEffect, useState } from 'react';
import axios from 'axios';

const PostComments = ({ postId }) => {
    const [comments, setComments] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchComments = async () => {
            try {
                const response = await axios.get(`http://localhost:8000/api/get_post_comments/${postId}/`);
                if (response.data.comments) {
                    setComments(response.data.comments);
                } else {
                    setComments([]);
                }
            } catch (err) {
                setError('Failed to fetch comments');
                console.error('Error fetching comments:', err);
            } finally {
                setLoading(false);
            }
        };

        fetchComments();
    }, [postId]);

    if (loading) {
        return <div className="text-center text-gray-500">Loading...</div>;
    }

    if (error) {
        return <div className="text-center text-red-500">{error}</div>;
    }

    return (
        <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-4">
            <div className="bg-white p-6 rounded-lg shadow-md w-full max-w-2xl">
                <h2 className="text-2xl font-bold mb-4 text-center">Post Comments</h2>
                {comments.length > 0 ? (
                    <ul>
                        {comments.map((comment) => (
                            <li key={comment.id} className="border-b border-gray-200 py-2">
                                <div className="flex flex-col">
                                    <span className="font-medium">{comment.author}</span>
                                    <span className="text-gray-600">{comment.content}</span>
                                </div>
                            </li>
                        ))}
                    </ul>
                ) : (
                    <div className="text-center text-gray-500">No comments available.</div>
                )}
            </div>
        </div>
    );
};

export default PostComments;
