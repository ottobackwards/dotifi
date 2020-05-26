import click


@click.command()
@click.option("--with-existing-dot-file", "-w", "existing_graph", required=False,
              help="Output will be based on an existing DOT graph definition as opposed to being built from NiFi",
              type=click.Path(exists=True, dir_okay=False, readable=True)
              )
@click.option("--with-conf-file", "-c", "conf_name", required=False,
              help="Path to the .yaml file with the configuration. All options can be set in the configuration, with ",
              type=click.Path(exists=True, dir_okay=False, readable=True)
              )
@click.option("--output-dot-file", "-o", "output_dot_name", default="./nifi-canvas.dot", required=False,
              help="Path to the dot file to store the dot results to.",
              type=click.Path(exists=False, dir_okay=False)
              )
@click.option("--output-graphviz-fmt", "-f", "output_graphviz_format", required=False, default="png",
              help="The format of the graphviz generated file. Formats (not all may be available on every system " +
                   "depending on how Graphviz was built)",
              type=click.Choice(["canon", "cmap", "cmapx", "cmapx_np", "dia", "dot", "fig", "gd", "gd2", "gif",
                                 "hpgl", "imap", "imap_np", "ismap", "jpe", "jpeg", "jpg", "mif", "mp", "pcl", "pdf",
                                 "pic", "plain", "plain-ext", "png", "ps", "ps2", "svg", "svgz", "vml", "vmlz", "vrml",
                                 "vtx", "wbmp", "xdot", "xlib"],
                                case_sensitive=True)
              )
@click.option("--output-graphviz-file", "-g", "output_graphviz_base_name", default="./nifi-canvas", required=False,
              help="Path to the dot file to store the graphviz results to. Results will be saved with the extension " +
                   "of the --output-graphviz-format option",
              type=click.Path(exists=False, dir_okay=False)
              )
@click.option("--start-at-pg", "-s", "starting_pg_id", required=False,
              help="The id of the process group to start at.  This will be a uuid.  When set the output will start " +
                   "with this process and it's descendents based on the depth setting",
              type=click.UUID
              )
@click.option("--depth", "-d", "depth", default="-1", required=False,
              help="The depth to descend to within nested process groups.  Note that the top level canvas " +
                   "is the root process group.  As such a depth of 0 will only output items in the root canvas and " +
                   "not any process groups it contains. A value of -1 means unlimited.", type=click.INT)
@click.option("--nifi-url", "-n", "nifi_url", default="http://localhost:8080/nifi", required=False,
              help="The url of the NiFi instance to connect to.  This is used if --with-existing is not set."
              )
@click.option("--using-ssl", "use_ssl", is_flag=True, required=False, default=False,
              help="Flag, when specified it signals that the NiFi connection requires SSL"
              )
@click.option("--using-user-pw", "use_user_pass", is_flag=True, required=False, default=False,
              help="Flag, when specified it signals that the NiFi connection requires a username and password"
              )
@click.option("--ca-file", "ca_file", required=False,
              help="A PEM file containing certs for the root CA(s) for the NiFi server",
              type=click.Path(exists=True, dir_okay=False, readable=True)
              )
@click.option("--client-cert-file", "client_cert_file", required=False,
              help="A PEM file containing the public certificates for the user / client identity",
              type=click.Path(exists=True, dir_okay=False, readable=True)
              )
@click.option("--client-key-file", "client_key_file", required=False,
              help="An encrypted (password -protected PEM file containing the client's secret key",
              type=click.Path(exists=True, dir_okay=False, readable=True)
              )
@click.option("--client-key-password", "client_key_password", required=False,
              help="The password to decrypt the client_key_file"
              )
@click.option("--nifi-username", "nifi_user_name", required=False,
              help="The NiFi user name"
              )
@click.option("--nifi-user-password", "nifi_user_password", required=False,
              help="The NiFi user password"
              )
def process(existing_graph, conf_name, output_dot_name, output_graphviz_format, output_graphviz_base_name,
            starting_pg_id, depth, nifi_url, use_ssl, use_user_pass, ca_file, client_cert_file, client_key_file,
            client_key_password, nifi_user_name, nifi_user_password):
    print("foo")


if __name__ == "__main__":
    process()
