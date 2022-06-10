import scala.io.Source
import scala.math
import $ivy.`org.scalactic::scalactic:3.2.12`
import $ivy.`org.scalatest::scalatest:3.2.12`
import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should
import scala.annotation.tailrec


object MaximumWeightIndependentSet {
  def sumNaive(path: IndexedSeq[Long]): Long = {
    path.size match {
      case 0 => 0
      case 1 => path(0)
      case n =>
        val s1 = sumNaive(path.slice(0, n-1)) 
        val s2 = sumNaive(path.slice(0, n-2)) + path(n-1)
        math.max(s1, s2)
    }
  }

  def sum(path: IndexedSeq[Long]): Long =
    weights(path, List(path(0), 0), 2).head

  @tailrec
  def weights(path: IndexedSeq[Long], low: List[Long], i: Int): List[Long] = {
    low match {
      case a :: b :: rest if i <= path.size =>
        weights(path, math.max(a, b + path(i-1)) :: low, i+1)
      case _ =>
        low
    }
  }
}

class MaximumWeightIndependentSetSpec extends AnyFlatSpec with should.Matchers {
  def readFixture(fileName: String): IndexedSeq[Long] = {
    // the first line is a header
    Source.fromFile(fileName).getLines().toIndexedSeq.tail.map(_.toLong)
  }


  "MaximumWeightIndependentSet.sumNaive" should "calculate sum of a small mwis" in {
    val path = readFixture("maximum-weight-independent-set-path-small.txt")
    val result = MaximumWeightIndependentSet.sumNaive(path)
    result should be (2617L)
  }

  "MaximumWeightIndependentSet.sum" should "calculate sum of a small mwis" in {
      val path = readFixture("maximum-weight-independent-set-path-small.txt")
      val result = MaximumWeightIndependentSet.sum(path)
      result should be (2617L)
    }

   it should "calculate sum of a large mwis" in {
    val path = readFixture("maximum-weight-independent-set-path.txt")
    val result = MaximumWeightIndependentSet.sum(path)
    result should be (2955353732L) 
    }
}

(new MaximumWeightIndependentSetSpec).execute() 

