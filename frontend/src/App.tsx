import React from 'react';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import Button from '@material-ui/core/Button';
import MaterialTable from 'material-table'
import { makeStyles } from '@material-ui/core/styles';

import api from './api';
import MaterialTableIcons from "./components/MaterialTableIcons";

const useStyles = makeStyles((theme) => ({
  root: {
    margin: theme.spacing(1),
    padding: theme.spacing(1),
  },
  table: {
    padding: theme.spacing(1),
  }
}));

enum ColumnDataType {
  THINGS,
  CATALOGS
}

function App() {
  const classes = useStyles();
  const [columnDataType, setColumnDataType] = React.useState<ColumnDataType>();
  const [things, setThings] = React.useState<Thing[]>([]);
  const [catalogs, setCatalogs] = React.useState<Catalog[]>([]);
  const [loadingData, setLoadingData] = React.useState<boolean>(false);

  async function getThings() {
    setLoadingData(true);
    fetch(api.THINGS)
    .then(res => res.json())
    .then(things => {
      setThings(things);
      setColumnDataType(ColumnDataType.THINGS)
    })
    .finally(() => setLoadingData(false));
  };

  async function getCatalogs() {
    setLoadingData(true);
    fetch(api.THINGS)
    .then(res => res.json())
    .then(things => {
      setCatalogs(things);
      setColumnDataType(ColumnDataType.CATALOGS)
    })
    .finally(() => setLoadingData(false));
  };

  const tableColumns = columnDataType === ColumnDataType.THINGS
  ? [
      {
        title: "Unique Identifer",
        field: "Unique Identifer"
      },
      {
        title: "Title",
        field: "Title"
      },
      {
        title: "Company",
        field: "Company"
      },
      {
        title: "Catalog",
        field: "Catalog"
      },
      {
        title: "Created At",
        field: "Created At"
      },
      {
        title: "Updated At",
        field: "Updated At"
      },
      {
        title: "Active?",
        field: "Active?"
      },
      {
        title: "Image URL",
        field: "Image URL"
      },
    ]
  : [
      {
        title: "Catalog",
        field: "Catalog"
      },
    ];

  const tableConfig = {
    columns: tableColumns,
    data: columnDataType === ColumnDataType.THINGS ? things : catalogs,
    title: columnDataType === ColumnDataType.THINGS ? "Things" : "Catalogs"
  };

  return (
    <>
      <Paper elevation={3} className={classes.root}>
        <Grid
          container
          direction="row"
          justify="space-evenly"
          alignItems="center"
          spacing={1}
        >
          <Button
            color="primary"
            onClick={getThings}
            variant="contained"
            disabled={loadingData}
          >
            Get Things
          </Button>
          <Button
            color="primary"
            onClick={getCatalogs}
            variant="contained"
            disabled={loadingData}
          >
            Get Catalogs
          </Button>
        </Grid>
      </Paper>
      <Grid item className={classes.table}>
        <MaterialTable
          options={{
            actionsColumnIndex: -1,
            search: true,
            padding: "dense",
            pageSize: 15,
            pageSizeOptions: [10, 15, 25, 50, 100],
            sorting: true,
            filtering: true,
            grouping: true
          }}
          isLoading={loadingData}
          icons={(MaterialTableIcons as any)}
          columns={tableConfig.columns}
          data={tableConfig.data}
          title={tableConfig.title}
        />
      </Grid>
    </>
  );
}

export default App;
