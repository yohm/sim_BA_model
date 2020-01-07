repo_dir = File.expand_path(File.dirname(__FILE__))

localhost = Host.find_by_name("localhost")

def create_sim( sim_params )
  if Simulator.where(name: sim_params[:name]).exists?
    puts "simulator #{sim_params[:name]} already exists" 
  else
    sim = Simulator.create!(sim_params)
    puts "simulator #{sim_params[:name]} has been created" 
  end
end

sim_params_BA = {
  name: "BA_model",
  command: "#{repo_dir}/run_BA.sh",
  support_input_json: true,
  print_version_command: "cd #{repo_dir} && git describe --always",
  parameter_definitions: [
    {key: "N", type: "Integer", default: 10000, description: "network size"},
    {key: "m", type: "Integer", default: 4,    description: "number of links"}
  ],
  description: "Barabasi-Albert model",
  executable_on: [ localhost ]
}

create_sim( sim_params_BA )

sim_params_BA_attractiveness = {
  name: "BA_attractiveness_model",
  command: "#{repo_dir}/run_BA_attractiveness.sh",
  support_input_json: true,
  print_version_command: "cd #{repo_dir} && git describe --always",
  parameter_definitions: [
    {key: "N", type: "Integer", default: 10000, description: "network size"},
    {key: "m", type: "Integer", default: 4,    description: "number of links"},
    {key: "A", type: "Integer", default: 0,    description: "initial attractiveness"}
  ],
  description: "Barabasi-Albert model having initial attractiveness",
  executable_on: [ localhost ]
}

create_sim( sim_params_BA_attractiveness )

sim_params_BA_extended = {
  name: "BA_extended_model",
  command: "#{repo_dir}/run_BA_extended.sh",
  support_input_json: false,
  print_version_command: "cd #{repo_dir} && git describe --always",
  parameter_definitions: [
    {key: "N", type: "Integer", default: 1000, description: "network size"},
    {key: "m", type: "Integer", default: 4,    description: "number of links"},
    {key: "p", type: "Float",   default: 0.0,  description: "Probability value for adding an edge between existing nodes. p + q < 1"},
    {key: "q", type: "Float",   default: 0.0,  description: "Probability value of rewiring of existing edges. p + q < 1"}
  ],
  description: "extended Barabasi-Albert model",
  executable_on: [ localhost ]
}

# create_sim( sim_params_BA_extended )
