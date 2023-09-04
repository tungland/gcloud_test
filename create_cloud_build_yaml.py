template = """steps:
 # Build the container image
 - name: 'gcr.io/cloud-builders/docker'
   args: ['build', '-t', 'gcr.io/{project_id}/{service_name}:$COMMIT_SHA', '.']
 # Push the container image to Container Registry
 - name: 'gcr.io/cloud-builders/docker'
   args: ['push', 'gcr.io/{project_id}/{service_name}:$COMMIT_SHA']
 # Deploy container image to Cloud Run
 - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
   entrypoint: gcloud
   args:
   - 'run'
   - 'deploy'
   - '{service_name}'
   - '--image'
   - 'gcr.io/{project_id}/{service_name}:$COMMIT_SHA'
   - '--region'
   - '{region}'
 images:
 - 'gcr.io/{project_id}/{service_name}:$COMMIT_SHA'
"""

def make_template(project_id, service_name, region):
    """Create a Cloud Build YAML file."""
    with open("cloudbuild.yaml", "w") as stream:
        stream.write(template.format(project_id=project_id, service_name=service_name, region=region))
        
        
        
if __name__ == "__main__":
    make_template("jupyterhub-379311", "gcloud-test", "europe-north1")
                     
                