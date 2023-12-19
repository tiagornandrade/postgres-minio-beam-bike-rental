package org.example.flink;

import org.apache.flink.api.common.typeinfo.TypeInformation;
import org.apache.flink.api.java.DataSet;
import org.apache.flink.api.java.ExecutionEnvironment;
import org.apache.flink.connector.jdbc.JdbcInputFormat;
import org.apache.flink.connector.jdbc.JdbcOutputFormat;
import org.apache.flink.api.java.tuple.Tuple5;
import org.apache.flink.configuration.Configuration;
import org.apache.flink.connector.jdbc.internal.JdbcOutputFormat;
import org.apache.flink.types.Row;

public class BatchDataTransformation {

    public static void main(String[] args) throws Exception {
        ExecutionEnvironment env = ExecutionEnvironment.getExecutionEnvironment();

        // Configuration for PostgreSQL
        Configuration configuration = new Configuration();
        configuration.setString("jdbc.url", "jdbc:postgresql://localhost:5432/postgresql");
        configuration.setString("jdbc.driver", "org.postgresql.Driver");
        configuration.setString("jdbc.username", "postgresql");
        configuration.setString("jdbc.password", "postgresql");

        env.getConfig().setGlobalJobParameters(configuration);

        // Define your SQL queries for each table
        String stationsSql = "SELECT * FROM stations";
//        String bikesSql = "SELECT * FROM bikes";
//        String tripsSql = "SELECT * FROM trips";

        // RowTypeInfo for each table
        TypeInformation<Row> stationsRowTypeInfo = TypeInformation.of(Row.class);
//        TypeInformation<Row> bikesRowTypeInfo = TypeInformation.of(Row.class);
//        TypeInformation<Row> tripsRowTypeInfo = TypeInformation.of(Row.class);

        // Read data from PostgreSQL
        DataSet<Tuple5<Integer, String, Double, Double, Integer>> stations =
                env.createInput(JdbcInputFormat.buildJdbcInputFormat()
                        .setDBUrl(configuration.getString("jdbc.url"))
                        .setDrivername(configuration.getString("jdbc.driver"))
                        .setUsername(configuration.getString("jdbc.username"))
                        .setPassword(configuration.getString("jdbc.password"))
                        .setQuery(stationsSql)
                        .setRowTypeInfo(stationsRowTypeInfo)
                        .finish());

//        DataSet<Tuple5<Integer, String, Double, Double, Integer>> bikes =
//                env.createInput(JdbcInputFormat.buildJdbcInputFormat()
//                        .setDBUrl(configuration.getString("jdbc.url"))
//                        .setDrivername(configuration.getString("jdbc.driver"))
//                        .setUsername(configuration.getString("jdbc.username"))
//                        .setPassword(configuration.getString("jdbc.password"))
//                        .setQuery(bikesSql)
//                        .setRowTypeInfo(bikesRowTypeInfo)
//                        .finish());
//
//        DataSet<Tuple5<Integer, String, Double, Double, Integer>> trips =
//                env.createInput(JdbcInputFormat.buildJdbcInputFormat()
//                        .setDBUrl(configuration.getString("jdbc.url"))
//                        .setDrivername(configuration.getString("jdbc.driver"))
//                        .setUsername(configuration.getString("jdbc.username"))
//                        .setPassword(configuration.getString("jdbc.password"))
//                        .setQuery(tripsSql)
//                        .setRowTypeInfo(tripsRowTypeInfo)
//                        .finish());


        // Define your output paths
        String stationsOutputPath = "s3a://trusted/stations.csv";
//        String bikesOutputPath = "s3a://trusted/bikes.csv";
//        String tripsOutputPath = "s3a://trusted/trips.csv";

        // Write data to PostgreSQL
        stations.output(JdbcOutputFormat.buildJdbcOutputFormat()
                .setDrivername(configuration.getString("jdbc.driver"))
                .setDBUrl(configuration.getString("jdbc.url"))
                .setUsername(configuration.getString("jdbc.username"))
                .setPassword(configuration.getString("jdbc.password"))
                .setQuery(stationsSql)
                .finish(), Tuple5::f0, Tuple5::f1, Tuple5::f2, Tuple5::f3, Tuple5::f4);

//        bikes.output(JdbcOutputFormat.buildJdbcOutputFormat()
//                .setDrivername(configuration.getString("jdbc.driver"))
//                .setDBUrl(configuration.getString("jdbc.url"))
//                .setUsername(configuration.getString("jdbc.username"))
//                .setPassword(configuration.getString("jdbc.password"))
//                .setQuery(bikesSql))

        // Execute the job
        env.execute("Batch Data Transformation");
        System.out.println("Job executed successfully.");
    }
}
