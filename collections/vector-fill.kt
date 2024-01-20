import java.time.Instant
import java.time.temporal.ChronoUnit

data class Data(val a: Long, val b: Long)

fun newData(x: Int): Data {
    return Data(x.toLong() / 2, x.toLong() / (x % 2 + 1).toLong())
}

fun main() {
    val startTime = Instant.now()
    //
    val vec = ArrayList<Data>(100_000)
    for (i in 0 until 100_000) {
        vec.add(newData(i))
    }
    //
    val endTime = Instant.now()
    val elapsedMicros = ChronoUnit.MICROS.between(startTime, endTime)
    println("$elapsedMicros")
}