
import loader;

if __name__ == '__main__':
    instance = loader.RequestModel(
        load_dir=False,
        dir="./",
        ignored_files=[],
        filename="requirements.txt",
        db_connection_string="postgres://user:postgres@127.0.0.1:5432/gpt?sslmode=disable",
        table_name="documents",
        vector_field="embedding",
        content_field="content"
    )
    loader.load_file(instance)
    

    
   