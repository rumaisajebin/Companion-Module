import axios from "axios";
import React, { useEffect, useState } from "react";

const ProfileList = () => {
  const [profiles, setProfiles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProfiles = async () => {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/api/Profile_list"
        );
        setProfiles(response.data);
        setLoading(false);
      } catch (error) {
        setError(error.message);
        setLoading(false);
      }
    };
    fetchProfiles();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h1>ProfileList</h1>
      <ul>
        {profiles.map((profile) => (
          <li key={profile.id}>
            <strong>Name:</strong> {profile.first_name} {profile.last_name}
            <br />
            <strong>Email:</strong> {profile.email}
            <br />
            <strong>Phone:</strong> {profile.phone_number}
            <br />
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProfileList;
