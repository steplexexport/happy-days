def run(arg_parser: argparse.ArgumentParser, version: str) -> None:
    args = arg_parser.parse_args()

    # setup logging
    date_fmt = "%d-%b-%y %H:%M:%S"
    logging_fmt = "%(asctime)s - %(levelname)s - %(message)s"
    logging_lvl = logging.DEBUG if args.v else logging.INFO
    logging.basicConfig(level=logging_lvl, format=logging_fmt, datefmt=date_fmt)

    # URL is a required argument
    if not args.url:
        arg_parser.print_help()
        sys.exit()#yes

    # Print verison then exit
    if args.version:
        print(f"TorBot Version: {version}")
        sys.exit()
 if args.save == "tree":
            tree.save()
        elif args.save == "json":
            tree.saveJSON()

        # always print something, table is the default
        if args.visualize == "table" or not args.visualize:
            tree.showTable()
        elif args.visualize == "tree":
            print(tree)
        elif args.visualize == "json":
            tree.showJSON()

    print("\n\n")
