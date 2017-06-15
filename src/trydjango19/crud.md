The acronym CRUD refers to all of the major functions that are implemented in relational database applications. Each letter in the acronym can map to a standard SQL statement, HTTP method (this is typically used to build RESTful APIs[5]) or DDS operation:

Operation	SQL	HTTP	DDS
Create	INSERT	PUT / POST	write
Read (Retrieve)	SELECT	GET	read / take
Update (Modify)	UPDATE	PUT / POST / PATCH	write
Delete (Destroy)	DELETE	DELETE	dispose


The comparison of the database oriented CRUD operations to HTTP methods has some flaws. Strictly speaking, both PUT and POST can create resources; the key difference is that POST leaves it for the server to decide at what URI to make the new resource available, whilst PUT dictates what URI to use; URIs are of course a concept that doesn't really line up with CRUD. The significant point about PUT is that it will replace whatever resource the URI was previously referring to with a brand new version, hence the PUT method being listed for Update as well. PUT is a 'replace' operation, which one could argue is not 'update'.
Although a relational database provides a common persistence layer in software applications, numerous other persistence layers exist. CRUD functionality can be implemented with an object database, an XML database, flat text files, custom file formats, tape, or card, for example.