db.createUser(
    {
        user: "m-search",
        pwd: "m-search",
        roles: [
            {
                role: "readWrite",
                db: "m-search"
            }
        ]
    }
);
