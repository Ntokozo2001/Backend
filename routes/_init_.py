from .job_routes import job_routes

def init_routes(app):
    app.register_blueprint(job_routes)
