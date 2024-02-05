import click
import os 

@click.command() 
@click.option('--input_directory',   '-i', type=click.Path(exists = True), required = True,  help = 'Path of the file which you want to convert..')
@click.option('--output_directory', '-o', help='Output path of the converted file.')
@click.option('--random', '-r', help = 'Just a random message')

def main(input_directory, output_directory, random): 
    # print(os.getcwd())
    # check if the input path exists or not 
    if not os.path.exists(input_directory) : 
        click.echo(f"There was an error : Couldn't fine the path : {input_directory}\nTry entering correct file path.")
    else : click.echo(input_directory)



if __name__ == '__main__':
    main()